from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Product, ProductCategory, DeliveryRequest
from .forms import DeliveryRequestForm

class HomeView(ListView):
    model = Product
    template_name = 'pages/home.html'
    context_object_name = 'featured_products'

    def get_queryset(self):
        return Product.objects.filter(is_on_sale=True)[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context

class ProductCatalogView(ListView):
    model = Product
    template_name = 'pages/catalog.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.request.GET.get('category')
        search_query = self.request.GET.get('q')

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['current_category'] = self.request.GET.get('category')
        context['search_query'] = self.request.GET.get('q')
        return context

class OrderCreateView(CreateView):
    model = DeliveryRequest
    form_class = DeliveryRequestForm
    template_name = 'pages/order_form.html'
    success_url = reverse_lazy('order_success')

    def get_initial(self):
        initial = super().get_initial()
        product_id = self.request.GET.get('product')
        if product_id:
            try:
                product = Product.objects.get(pk=product_id)
                initial['selected_product'] = product.pk
            except (Product.DoesNotExist, ValueError):
                pass
        return initial

class OrderSuccessView(TemplateView):
    template_name = 'pages/success.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class ContactView(TemplateView):
    template_name = 'pages/contact.html'
