from django import forms
from .models import CourseEnrollment, Course

class CourseEnrollmentForm(forms.ModelForm):
    class Meta:
        model = CourseEnrollment
        fields = ['student_name', 'phone_number', 'email', 'selected_course', 'message']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Аты-жөніңіз'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (___) ___-__-__'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.kz'}),
            'selected_course': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Қосымша сұрақтарыңыз болса жазыңыз...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['selected_course'].empty_label = "Курсты таңдаңыз"
