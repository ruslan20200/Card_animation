from django import forms
from .models import EnrollmentRequest

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = EnrollmentRequest
        fields = ['parent_name', 'phone_number', 'child_name', 'child_age', 'selected_group', 'message']
        widgets = {
            'parent_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ата-ананың аты-жөні'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (7XX) XXX-XX-XX'}),
            'child_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Баланың аты-жөні'}),
            'child_age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Жасы'}),
            'selected_group': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Қосымша мәліметтер...'}),
        }
