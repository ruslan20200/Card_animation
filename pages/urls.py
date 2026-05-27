from django.urls import path
from .views import (
    HomePageView,
    RatesPageView,
    AboutPageView,
    ContactPageView,
    ReservationCreateView
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("rates/", RatesPageView.as_view(), name="rates"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("reserve/", ReservationCreateView.as_view(), name="reserve"),
]
