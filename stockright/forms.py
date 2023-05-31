from django import forms
from stockright.models import StockingDensity, Pond

class DensityForm(forms.ModelForm):
    class Meta:
        model = StockingDensity
        fields = ['length', 'width', 'height']
        labels = {'length': 'Length in feet', 'width':'Width in feet', 'height':'Height in feet'}

    def clean(self):
        cleaned_data=super().clean()
        length = cleaned_data.get('length')
        if length is None:
            raise  forms.ValidationError('These fields cannot be blank.')
        return length


#Model Pond form
class PondForm(forms.ModelForm):
    class Meta:
        model = Pond
        fields = ['name']
        label = {'name': 'Enter a pond name'}

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and Pond.objects.filter(name__icontains=name).exists():
            raise forms.ValidationError('A pond with this name already exists. Choose a new name')
        return name
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
