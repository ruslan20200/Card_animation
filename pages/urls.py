from django.urls import path
from .views import (
    HomePageView,
    BookListView,
    BookDetailView,
    AuthorListView,
    AuthorDetailView,
    BookReservationView,
    ReservationSuccessView,
    AboutView,
    ContactView
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("books/", BookListView.as_view(), name="book_list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("authors/", AuthorListView.as_view(), name="author_list"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author_detail"),
    path("reserve/", BookReservationView.as_view(), name="book_reservation"),
    path("reserve/success/", ReservationSuccessView.as_view(), name="reservation_success"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
]
