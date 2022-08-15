from django import forms
from .models import Vegetables as VegetablesProduct


class VegetableCreateForm(forms.ModelForm):
    class Meta:
        model = VegetablesProduct
        exclude = ('category',)


