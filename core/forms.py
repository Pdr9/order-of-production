from django import forms
from .models import Pessoa

class AddForm(forms.ModelForm):
    data = forms.DateField(label="Data", widget=forms.DateInput(attrs={'type': 'date'}))
    date_shipment = forms.DateField(label="Date Shipment", widget=forms.DateInput(attrs={'type': 'date'}))
    approval_date = forms.DateField(label="Approval Date", widget=forms.DateInput(attrs={'type': 'date'}))
    date_payment = forms.DateField(label="Date Payment", widget=forms.DateInput(attrs={'type': 'date'}))
    preview_payment = forms.DateField(label="Preview Payment", widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Pessoa
        fields = '__all__'
##adicionar campo choices em aprovado/aguardando/pago
