from django.urls import path
from .views import HomeView, CatalogView, OrderCreateView, OrderSuccessView, AboutView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('order/', OrderCreateView.as_view(), name='order'),
    path('order/success/', OrderSuccessView.as_view(), name='order_success'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
