from django import forms
from .models import BookingRequest

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = [
            'guest_name', 'phone_number', 'email', 'selected_room_type',
            'check_in_date', 'check_out_date', 'guest_count'
        ]
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'guest_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'selected_room_type': forms.Select(attrs={'class': 'form-select'}),
            'guest_count': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get('check_in_date')
        check_out_date = cleaned_data.get('check_out_date')

        if check_in_date and check_out_date:
            if check_out_date <= check_in_date:
                raise forms.ValidationError(
                    "Кету күні келу күнінен кешірек болуы керек.",
                    code='invalid_dates'
                )
        return cleaned_data
