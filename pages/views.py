from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.urls import reverse_lazy
from .models import Category, AutoPart, ContactMessage

class HomeView(ListView):
    model = AutoPart
    template_name = "pages/home.html"
    context_object_name = "featured_parts"

    def get_queryset(self):
        return AutoPart.objects.filter(is_featured=True, is_available=True)[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

class CatalogView(ListView):
    model = AutoPart
    template_name = "pages/catalog.html"
    context_object_name = "parts"
    paginate_by = 12

    def get_queryset(self):
        queryset = AutoPart.objects.filter(is_available=True)
        category_id = self.request.GET.get("category")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["selected_category"] = self.request.GET.get("category")
        return context

class PartDetailView(DetailView):
    model = AutoPart
    template_name = "pages/part_detail.html"
    context_object_name = "part"

class ContactView(CreateView):
    model = ContactMessage
    fields = ["name", "email", "subject", "message"]
    template_name = "pages/contact.html"
    success_url = reverse_lazy("contact_success")

class ContactSuccessView(TemplateView):
    template_name = "pages/contact_success.html"
