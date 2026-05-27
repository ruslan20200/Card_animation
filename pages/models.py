from django.db import models
from django.urls import reverse

class Author(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Толық аты-жөні")
    bio = models.TextField(verbose_name="Өмірбаяны")
    photo_url = models.URLField(verbose_name="Фото URL")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторлар"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})

class Book(models.Model):
    GENRE_CHOICES = [
        ("Көркем әдебиет", "Көркем әдебиет"),
        ("Ғылыми", "Ғылыми"),
        ("Тұлғалық даму", "Тұлғалық даму"),
        ("Тарих", "Тарих"),
        ("Поэзия", "Поэзия"),
    ]

    title = models.CharField(max_length=255, verbose_name="Атауы")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books", verbose_name="Авторы")
    description = models.TextField(verbose_name="Сипаттамасы")
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, verbose_name="Жанры")
    publication_year = models.IntegerField(verbose_name="Басылым жылы")
    is_available = models.BooleanField(default=True, verbose_name="Қолжетімді")
    cover_image_url = models.URLField(verbose_name="Мұқаба URL")

    class Meta:
        verbose_name = "Кітап"
        verbose_name_plural = "Кітаптар"
        ordering = ["-id"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})

class BookReservation(models.Model):
    reader_name = models.CharField(max_length=255, verbose_name="Оқырман есімі")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон нөмірі")
    email = models.EmailField(verbose_name="Электрондық пошта")
    selected_book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Таңдалған кітап")
    pickup_date = models.DateField(verbose_name="Алу күні")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Құрылған уақыты")

    class Meta:
        verbose_name = "Брондау"
        verbose_name_plural = "Брондаулар"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.reader_name} - {self.selected_book.title}"
