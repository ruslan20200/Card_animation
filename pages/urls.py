from django.urls import path
from .views import (
    HomePageView,
    MedicineCatalogView,
    MedicineDetailView,
    OrderRequestCreateView,
    OrderSuccessView,
    AboutPageView,
    ContactPageView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('catalog/', MedicineCatalogView.as_view(), name='catalog'),
    path('medicine/<int:pk>/', MedicineDetailView.as_view(), name='medicine_detail'),
    path('order/', OrderRequestCreateView.as_view(), name='order_form'),
    path('order/success/', OrderSuccessView.as_view(), name='order_success'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
