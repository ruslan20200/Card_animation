from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Санат атауы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Санат"
        verbose_name_plural = "Санаттар"
        ordering = ['name']

class AutoPart(models.Model):
    name = models.CharField(max_length=200, verbose_name="Бөлшек атауы")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="parts", verbose_name="Санаты")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Бағасы")
    description = models.TextField(verbose_name="Сипаттамасы")
    is_available = models.BooleanField(default=True, verbose_name="Қолжетімді")
    is_featured = models.BooleanField(default=False, verbose_name="Таңдаулы")
    image_url = models.URLField(max_length=500, verbose_name="Сурет сілтемесі")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автобөлшек"
        verbose_name_plural = "Автобөлшектер"
        ordering = ['-created_at']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Аты-жөні")
    email = models.EmailField(verbose_name="Электрондық пошта")
    subject = models.CharField(max_length=200, verbose_name="Тақырыбы")
    message = models.TextField(verbose_name="Хабарлама")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Жіберілген уақыты")

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = "Байланыс хабарламасы"
        verbose_name_plural = "Байланыс хабарламалары"
        ordering = ['-created_at']
