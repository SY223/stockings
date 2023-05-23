from django.shortcuts import render
from stockright.models import StockingDensity, Pond
from stockright.forms import DensityForm, PondForm
from stockright.pond_logic import pondvolume
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'stockright/index.html')

def ponds(request):
    '''show all ponds of a single user'''
    pond_type = Pond.objects.filter(owner=request.user).order_by('name')
    context = {'pond_type':pond_type}
    return render(request, 'stockright/ponds.html', context)

def pond(request, pond_id):
    pond = Pond.objects.get(id=pond_id)
    if pond.owner != request.user:
        raise Http404
    densities = pond.stockingdensity_set.order_by('-date_checked')
    context = {'pond':pond, 'densities':densities}
    return render(request, 'stockright/pond.html', context)

def new_pond(request):
    '''create a new pond'''
    if request.method != 'POST':
        form = PondForm()
    else:
        form = PondForm(request.POST)
        if form.is_valid():
            new_pond = form.save(commit=False)
            new_pond.owner = request.user
            new_pond.save()
            return HttpResponseRedirect(reverse('stockright:ponds'))
    context={'form':form}
    return render(request, 'stockright/crud/add_pond.html', context)


def check_stock(request, pond_id):
    pond = Pond.objects.get(id=pond_id)
    if request.method != 'POST':
        form = DensityForm()
    else:
        form = DensityForm(request.POST)
        if form.is_valid():
            new_check = form.save(commit=False)
            new_check.pond = pond
            new_check.to_stock = pondvolume(new_check.length, new_check.width, new_check.height)
            new_check.verdict = f'You can humbly stock {new_check.to_stock} fishes.'
            new_check.save()
            return HttpResponseRedirect(reverse('stockright:pond', args=[pond.id]))
    context = {'pond':pond,'form':form}
    return render(request, 'stockright/check_stock.html', context)


def delete_density(request, stock_id):
    density = StockingDensity.objects.get(id=stock_id)
    density.delete()
    return HttpResponseRedirect(reverse('stockright:pond', args=[density.pond.id]))

  