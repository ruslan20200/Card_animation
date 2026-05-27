from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import ServiceCategory, BeautyService, Stylist, Appointment
from django import forms

class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_services'] = BeautyService.objects.filter(is_popular=True)[:4]
        context['top_stylists'] = Stylist.objects.filter(is_top=True)[:3]
        return context

class ServiceCatalogView(ListView):
    model = BeautyService
    template_name = "pages/catalog.html"
    context_object_name = "services"

    def get_queryset(self):
        category_id = self.request.GET.get('category')
        if category_id:
            return BeautyService.objects.filter(category_id=category_id)
        return BeautyService.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ServiceCategory.objects.all()
        context['selected_category'] = self.request.GET.get('category')
        return context

class StylistListView(ListView):
    model = Stylist
    template_name = "pages/stylists.html"
    context_object_name = "stylists"

class AboutView(TemplateView):
    template_name = "pages/about.html"

class ContactView(TemplateView):
    template_name = "pages/contact.html"

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['client_name', 'phone_number', 'selected_service', 'selected_stylist', 'appointment_date', 'appointment_time']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Сіздің атыңыз'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (7xx) xxx-xx-xx'}),
            'selected_service': forms.Select(attrs={'class': 'form-select'}),
            'selected_stylist': forms.Select(attrs={'class': 'form-select'}),
        }

class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = "pages/appointment_form.html"
    success_url = reverse_lazy('appointment_success')

    def get_initial(self):
        initial = super().get_initial()
        service_id = self.request.GET.get('service')
        stylist_id = self.request.GET.get('stylist')
        if service_id:
            initial['selected_service'] = service_id
        if stylist_id:
            initial['selected_stylist'] = stylist_id
        return initial

class AppointmentSuccessView(TemplateView):
    template_name = "pages/appointment_success.html"
