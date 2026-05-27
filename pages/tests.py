from django.test import TestCase
from django.urls import reverse
from .models import Author, Book

class LibraryTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            full_name="Тест Авторы",
            bio="Тест өмірбаяны",
            photo_url="http://example.com/photo.jpg"
        )
        self.book = Book.objects.create(
            title="Тест Кітабы",
            author=self.author,
            description="Тест сипаттамасы",
            genre="Көркем әдебиет",
            publication_year=2023,
            cover_image_url="http://example.com/cover.jpg"
        )

    def test_pages_load(self):
        pages = [
            reverse("home"),
            reverse("book_list"),
            reverse("book_detail", kwargs={"pk": self.book.pk}),
            reverse("author_list"),
            reverse("author_detail", kwargs={"pk": self.author.pk}),
            reverse("book_reservation"),
            reverse("reservation_success"),
            reverse("about"),
            reverse("contact"),
        ]
        for url in pages:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, f"Page {url} failed to load")

    def test_book_search(self):
        url = reverse("book_list") + "?q=Тест"
        response = self.client.get(url)
        self.assertContains(response, "Тест Кітабы")

    def test_book_reservation_initial(self):
        url = reverse("book_reservation") + f"?book_id={self.book.id}"
        response = self.client.get(url)
        self.assertContains(response, "Тест Кітабы")
