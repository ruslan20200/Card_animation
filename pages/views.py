from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from .models import Currency, ExchangeReservation

class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['currencies'] = Currency.objects.filter(is_active=True)
        return context

class RatesPageView(ListView):
    model = Currency
    template_name = "pages/rates.html"
    context_object_name = "currencies"
    queryset = Currency.objects.filter(is_active=True)

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class ContactPageView(TemplateView):
    template_name = "pages/contact.html"

class ReservationCreateView(CreateView):
    model = ExchangeReservation
    template_name = "pages/reserve.html"
    fields = ['client_name', 'phone_number', 'source_currency', 'operation_type', 'amount_to_exchange', 'expected_amount']
    success_url = reverse_lazy('home')

    def get_initial(self):
        initial = super().get_initial()
        currency_code = self.request.GET.get('currency')
        if currency_code:
            try:
                currency = Currency.objects.get(code=currency_code, is_active=True)
                initial['source_currency'] = currency
            except Currency.DoesNotExist:
                pass

        operation = self.request.GET.get('operation')
        if operation in ['buy', 'sell']:
            initial['operation_type'] = operation

        return initial
