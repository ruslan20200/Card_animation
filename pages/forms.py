from django import forms
from .models import BookReservation, Book

class BookReservationForm(forms.ModelForm):
    class Meta:
        model = BookReservation
        fields = ["reader_name", "phone_number", "email", "selected_book", "pickup_date"]
        widgets = {
            "pickup_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "reader_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "selected_book": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["selected_book"].queryset = Book.objects.filter(is_available=True)
