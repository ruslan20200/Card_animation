from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Book, Author, BookReservation
from .forms import BookReservationForm

class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_books"] = Book.objects.all()[:4]
        context["popular_authors"] = Author.objects.all()[:3]
        return context

class BookListView(ListView):
    model = Book
    template_name = "pages/book_list.html"
    context_object_name = "books"
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        genre = self.request.GET.get("genre")

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(author__full_name__icontains=query)
            )

        if genre:
            queryset = queryset.filter(genre=genre)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = [choice[0] for choice in Book.GENRE_CHOICES]
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = "pages/book_detail.html"
    context_object_name = "book"

class AuthorListView(ListView):
    model = Author
    template_name = "pages/author_list.html"
    context_object_name = "authors"

class AuthorDetailView(DetailView):
    model = Author
    template_name = "pages/author_detail.html"
    context_object_name = "author"

class BookReservationView(CreateView):
    model = BookReservation
    form_class = BookReservationForm
    template_name = "pages/book_reservation.html"
    success_url = reverse_lazy("reservation_success")

    def get_initial(self):
        initial = super().get_initial()
        book_id = self.request.GET.get("book_id")
        if book_id:
            try:
                initial["selected_book"] = Book.objects.get(id=book_id, is_available=True)
            except Book.DoesNotExist:
                pass
        return initial

class ReservationSuccessView(TemplateView):
    template_name = "pages/reservation_success.html"

class AboutView(TemplateView):
    template_name = "pages/about.html"

class ContactView(TemplateView):
    template_name = "pages/contact.html"
