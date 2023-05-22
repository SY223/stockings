from django.shortcuts import render
from stockright.models import StockingDensity, Pond
from stockright.forms import DensityForm
from stockright.pond_logic import pondvolume
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'stockright/index.html')

def ponds(request):
    pond_type = Pond.objects.order_by('name')
    context = {'pond_type':pond_type}
    return render(request, 'stockright/ponds.html', context)

def pond(request, pond_id):
    pond = Pond.objects.get(id=pond_id)
    densities = pond.stockingdensity_set.order_by('-date_checked')
    context = {'pond':pond, 'densities':densities}
    return render(request, 'stockright/pond.html', context)

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




  
# if form.is_valid():
#     length = form.cleaned_data['length']
#     width = form.cleaned_data['width']
#     height = form.cleaned_data['height']
#     to_stock = pondvolume(length, width, height)
#     request.session['to_stock'] = to_stock
#     stocking_density = StockingDensity(length=length, width=width, height=height, to_stock=to_stock)
#     stocking_density.save()
#     return redirect(resultPage)
# else:
# form = DensityForm()