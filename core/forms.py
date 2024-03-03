from django import forms
from .models import Pessoa

class AddForm(forms.ModelForm):
    # Campos de data com widgets de entrada de data
    data = forms.DateField(label="Data", widget=forms.DateInput(attrs={'type': 'date'}))
    date_shipment = forms.DateField(label="Date Shipment", widget=forms.DateInput(attrs={'type': 'date'}))
    approval_date = forms.DateField(label="Approval Date", widget=forms.DateInput(attrs={'type': 'date'}))
    date_payment = forms.DateField(label="Date Payment", widget=forms.DateInput(attrs={'type': 'date'}))
    preview_payment = forms.DateField(label="Preview Payment", widget=forms.DateInput(attrs={'type': 'date'}))
    
    # Campos de escolha para status de aprovação e status de pagamento
    PAYMENT_CHOICES = (
        ('pendente', 'Pendente'),
        ('recebido', 'Recebido'),
        ('atrasado', 'Atrasado'),
    )
    payment_status = forms.ChoiceField(label="Status de Pagamento", choices=PAYMENT_CHOICES)
    
    class Meta:
        model = Pessoa
        fields = '__all__'
