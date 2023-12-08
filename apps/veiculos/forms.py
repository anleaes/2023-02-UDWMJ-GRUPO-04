from django import forms
from .models import Veiculo

class VeiculoForm(forms.ModelForm):

    class Meta:
        model = Veiculo
        exclude = ('created_on' , 'updated_on',)