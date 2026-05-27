from django import forms
from .models import DeliveryRequest

class DeliveryRequestForm(forms.ModelForm):
    class Meta:
        model = DeliveryRequest
        fields = ['customer_name', 'phone_number', 'delivery_address', 'selected_product', 'quantity']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Аты-жөніңіз'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (7xx) xxx-xx-xx'}),
            'delivery_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Жеткізу мекенжайы'}),
            'selected_product': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("Саны 0-ден көп болуы керек.")
        if quantity > 50:
            raise forms.ValidationError("Бір тапсырыста 50-ден көп тауар алуға болмайды.")
        return quantity
