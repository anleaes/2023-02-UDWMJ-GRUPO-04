from django import forms
from .models import Reserve, Clients, ReserveItem ,Payment
class ReserveForm(forms.ModelForm):
    
    class Meta:
        model = Reserve
        exclude = ('clients', 'created_on' , 'updated_on')

class ReserveItemForm(forms.ModelForm):
    
    class Meta:
        model = ReserveItem
        exclude = ('reserve', 'created_on' , 'updated_on')
