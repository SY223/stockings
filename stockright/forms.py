from django import forms
from stockright.models import StockingDensity

class DensityForm(forms.ModelForm):
    class Meta:
        model = StockingDensity
        fields = ['length', 'width', 'height']
        labels = {'length': 'Length', 'width':'Width', 'height':'Height'}
