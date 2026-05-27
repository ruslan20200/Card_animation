from django.contrib import admin
from .models import Author, Book, BookReservation

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("full_name",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre", "publication_year", "is_available")
    list_filter = ("genre", "is_available")
    search_fields = ("title", "author__full_name")

@admin.register(BookReservation)
class BookReservationAdmin(admin.ModelAdmin):
    list_display = ("reader_name", "selected_book", "pickup_date", "created_at")
    list_filter = ("pickup_date", "created_at")
    search_fields = ("reader_name", "selected_book__title")
