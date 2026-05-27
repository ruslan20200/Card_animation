from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import JewelryItem, JewelryCategory, JewelryOrderRequest
from .forms import JewelryOrderForm

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['handcrafted_items'] = JewelryItem.objects.filter(is_handcrafted=True)[:4]
        context['categories'] = JewelryCategory.objects.all()
        return context

class CatalogView(ListView):
    model = JewelryItem
    template_name = 'catalog.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        material = self.request.GET.get('material')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if material:
            queryset = queryset.filter(material=material)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = JewelryCategory.objects.all()
        context['materials'] = JewelryItem.MATERIAL_CHOICES
        context['selected_category'] = self.request.GET.get('category')
        context['selected_material'] = self.request.GET.get('material')
        return context

class OrderCreateView(CreateView):
    model = JewelryOrderRequest
    form_class = JewelryOrderForm
    template_name = 'order_form.html'
    success_url = reverse_lazy('order_success')

    def get_initial(self):
        initial = super().get_initial()
        item_id = self.request.GET.get('item')
        if item_id:
            initial['selected_item'] = item_id
        return initial

class OrderSuccessView(TemplateView):
    template_name = 'order_success.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'
