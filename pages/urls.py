from django.urls import path
from .views import (
    HomePageView,
    ServiceCatalogView,
    StylistListView,
    AboutView,
    ContactView,
    AppointmentCreateView,
    AppointmentSuccessView
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("catalog/", ServiceCatalogView.as_view(), name="catalog"),
    path("stylists/", StylistListView.as_view(), name="stylists"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("appointment/", AppointmentCreateView.as_view(), name="appointment"),
    path("appointment/success/", AppointmentSuccessView.as_view(), name="appointment_success"),
]
