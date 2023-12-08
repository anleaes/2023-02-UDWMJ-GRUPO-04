from django import forms
from .models import Rentalcompany

class RentalcompanyForm(forms.ModelForm):

    class Meta:
        model = Rentalcompany
        exclude = ('created_on' , 'updated_on',)