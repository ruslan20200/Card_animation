from django.urls import path
from .views import HomeView, CatalogView, PartDetailView, ContactView, ContactSuccessView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("catalog/", CatalogView.as_view(), name="catalog"),
    path("part/<int:pk>/", PartDetailView.as_view(), name="part_detail"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("contact/success/", ContactSuccessView.as_view(), name="contact_success"),
]
