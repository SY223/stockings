from django import forms
from stockright.models import StockingDensity, Pond

class DensityForm(forms.ModelForm):
    class Meta:
        model = StockingDensity
        fields = ['length', 'width', 'height']
        labels = {'length': 'Length in feet', 'width':'Width in feet', 'height':'Height in feet'}

class PondForm(forms.ModelForm):
    class Meta:
        model = Pond
        fields = ['name']
        label = {'name': 'Enter a pond name'}
