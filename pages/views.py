from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Medicine, MedicineCategory, OrderRequest
from .forms import OrderRequestForm

class HomePageView(ListView):
    model = Medicine
    template_name = "pages/home.html"
    context_object_name = "featured_medicines"

    def get_queryset(self):
        return Medicine.objects.filter(is_featured=True, is_available=True)[:4]

class MedicineCatalogView(ListView):
    model = Medicine
    template_name = "pages/catalog.html"
    context_object_name = "medicines"
    paginate_by = 12

    def get_queryset(self):
        queryset = Medicine.objects.filter(is_available=True)
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = MedicineCategory.objects.all()
        context['selected_category'] = self.request.GET.get('category')
        return context

class MedicineDetailView(DetailView):
    model = Medicine
    template_name = "pages/medicine_detail.html"
    context_object_name = "medicine"

class OrderRequestCreateView(CreateView):
    model = OrderRequest
    form_class = OrderRequestForm
    template_name = "pages/order_form.html"
    success_url = reverse_lazy('order_success')

    def get_initial(self):
        initial = super().get_initial()
        medicine_id = self.request.GET.get('medicine')
        if medicine_id:
            try:
                medicine = Medicine.objects.get(id=medicine_id)
                initial['medicine_name'] = medicine.name
            except Medicine.DoesNotExist:
                pass
        return initial

class OrderSuccessView(TemplateView):
    template_name = "pages/order_success.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class ContactPageView(TemplateView):
    template_name = "pages/contact.html"
