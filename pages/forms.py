from django import forms
from .models import OrderRequest

class OrderRequestForm(forms.ModelForm):
    class Meta:
        model = OrderRequest
        fields = ['customer_name', 'phone_number', 'medicine_name']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Атыңыз'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (7xx) xxx-xx-xx'}),
            'medicine_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Дәрі атауы немесе сұрақ'}),
        }
