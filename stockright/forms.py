from django import forms
from stockright.models import StockingDensity, Pond
from django.utils.translation import gettext_lazy as _

class DensityForm(forms.ModelForm):
    class Meta:
        model = StockingDensity
        fields = ['length', 'width', 'height']
        labels = {'length': 'Length in feet', 'width':'Width in feet', 'height':'Height in feet',}
    
    def clean_length(self):
        length = self.cleaned_data.get('length')
        if length is not None and length <= 0:
            raise forms.ValidationError(_('Length must be a positive value and not zero.'))
        return length
    
    def clean_width(self):
        width = self.cleaned_data.get('width')
        if width is not None and width <= 0:
            raise forms.ValidationError(_('Width must be a positive value and not zero.'))
        return width
    
    def clean_height(self):
        height = self.cleaned_data.get('height')
        if height is not None and height <= 0:
            raise forms.ValidationError(_('Height must be a positive value and not zero.'))
        return height




#Model Pond form
class PondForm(forms.ModelForm):
    class Meta:
        model = Pond
        fields = ['name']
        label = {'name': 'Enter a pond name'}
