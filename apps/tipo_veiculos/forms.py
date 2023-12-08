from django import forms
from .models import TipoVeiculos

class TipoVeiculosForm(forms.ModelForm):

    class Meta:
        model = TipoVeiculos
        exclude = ('created_on' , 'updated_on',)