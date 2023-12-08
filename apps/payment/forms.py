from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        exclude = ('created_on' , 'updated_on',)