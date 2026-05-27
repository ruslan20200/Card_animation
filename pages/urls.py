from django.urls import path
from .views import (
    HomePageView, RoomCatalogView, RoomDetailView,
    BookingCreateView, BookingSuccessView, AboutView, ContactView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('rooms/', RoomCatalogView.as_view(), name='room_catalog'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('book/', BookingCreateView.as_view(), name='booking_form'),
    path('book/success/', BookingSuccessView.as_view(), name='booking_success'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
