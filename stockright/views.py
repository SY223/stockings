from django.shortcuts import render, get_object_or_404
from stockright.models import StockingDensity, Pond
from stockright.forms import DensityForm, PondForm
from stockright.pond_logic import pondvolume, thirty_p_decrease, twenty_p_decrease
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    return render(request, 'stockright/index.html')

@login_required
def ponds(request):
    '''show all ponds of a single user'''
    pond_type = Pond.objects.filter(owner=request.user).order_by('name')
    context = {'pond_type':pond_type}
    return render(request, 'stockright/ponds.html', context)

@login_required
def pond(request, pond_id):
    # pond = Pond.objects.get(id=pond_id)
    # if pond.owner != request.user:
    #     raise Http404
    pond = get_object_or_404(Pond, owner=request.user, id=pond_id)
    densities = pond.stockingdensity_set.order_by('-date_checked')
    context = {'pond':pond, 'densities':densities}
    return render(request, 'stockright/pond.html', context)

@login_required
def new_pond(request):
    '''create a new pond'''
    if request.method != 'POST':
        form = PondForm()
    else:
        form = PondForm(data=request.POST)
        if form.is_valid():
            pond_name = form.cleaned_data['name']
            if Pond.objects.filter(owner=request.user, name__icontains=pond_name).exists():
                form.add_error('name', 'A pond with this name already exists.')
            else:
                new_pond = form.save(commit=False)
                new_pond.owner = request.user
                new_pond.save()
                return HttpResponseRedirect(reverse('stockright:ponds'))
    context={'form':form}
    return render(request, 'stockright/crud/add_pond.html', context)

@login_required
def edit_pond_name(request, pond_id):
    pond = Pond.objects.get(id=pond_id)
    name = pond.name
    if pond.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = PondForm(instance=pond)
    else:
        form = PondForm(instance=pond, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('stockright:ponds'))
    context = {'pond':pond, 'name':name, 'form':form}
    return render(request, 'stockright/crud/edit_pond_name.html', context)

@login_required
def delete_pond(request, pond_id):
    pond = Pond.objects.get(id=pond_id)
    owner = pond.owner
    if owner != request.user:
        raise Http404
    pond.delete()
    return HttpResponseRedirect(reverse('stockright:ponds'))

@login_required
def check_stock(request, pond_id):
    pond = Pond.objects.get(id=pond_id)
    if request.method != 'POST':
        form = DensityForm()
    else:
        form = DensityForm(data=request.POST)
        if form.is_valid():
            new_check = form.save(commit=False)
            new_check.pond = pond
            new_check.to_stock = pondvolume(new_check.length, new_check.width, new_check.height)
            new_check.verdict = f'You can humbly stock {new_check.to_stock} fishes.'
            new_check.twenty_percent_decrease = twenty_p_decrease(new_check.to_stock)
            new_check.thirty_percent_decrease = thirty_p_decrease(new_check.to_stock)
            new_check.save()
            return HttpResponseRedirect(reverse('stockright:pond', args=[pond.id]))
    context = {'pond':pond,'form':form}
    return render(request, 'stockright/check_stock.html', context)

@login_required
def edit_density(request, stock_id):
    density = StockingDensity.objects.get(id=stock_id)
    pond = density.pond
    if pond.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = DensityForm(instance=density)
    else:
        form = DensityForm(instance=density, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('stockright:pond', args=[pond.id]))
    context = {'density':density, 'pond':pond, 'form':form}
    return render(request, 'stockright/crud/edit_density.html', context)


@login_required
def delete_density(request, stock_id):
    density = StockingDensity.objects.get(id=stock_id)
    owner = density.pond.owner
    if owner != request.user:
        raise Http404
    density.delete()
    return HttpResponseRedirect(reverse('stockright:pond', args=[density.pond.id]))


  