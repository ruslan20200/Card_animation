from django import forms
from .models import JewelryOrderRequest, JewelryItem

class JewelryOrderForm(forms.ModelForm):
    class Meta:
        model = JewelryOrderRequest
        fields = ['customer_name', 'phone_number', 'selected_item', 'preferred_size', 'preferred_contact_method', 'message']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Сіздің есіміңіз'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон нөміріңіз'}),
            'selected_item': forms.Select(attrs={'class': 'form-select'}),
            'preferred_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Өлшемі (мысалы, 17.5)'}),
            'preferred_contact_method': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Қосымша тілектеріңіз...'}),
        }
