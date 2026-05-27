from django.db import models

class MedicineCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория атауы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дәрі-дәрмек категориясы"
        verbose_name_plural = "Дәрі-дәрмек категориялары"
        ordering = ['name']

class Medicine(models.Model):
    name = models.CharField(max_length=200, verbose_name="Атауы")
    category = models.ForeignKey(MedicineCategory, on_delete=models.CASCADE, related_name='medicines', verbose_name="Категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Бағасы (тг)")
    description = models.TextField(verbose_name="Сипаттамасы")
    requires_prescription = models.BooleanField(default=False, verbose_name="Рецепт қажет пе?")
    is_available = models.BooleanField(default=True, verbose_name="Қолжетімді ме?")
    is_featured = models.BooleanField(default=False, verbose_name="Басты бетте көрсету")
    image_url = models.URLField(max_length=500, verbose_name="Сурет сілтемесі (Unsplash)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дәрі"
        verbose_name_plural = "Дәрілер"
        ordering = ['name']

class OrderRequest(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name="Клиенттің аты")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон нөмірі")
    medicine_name = models.CharField(max_length=200, verbose_name="Дәрі атауы / Хабарлама")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Құрылған уақыты")

    def __str__(self):
        return f"{self.customer_name} - {self.medicine_name}"

    class Meta:
        verbose_name = "Тапсырысқа өтінім"
        verbose_name_plural = "Тапсырысқа өтінімдер"
        ordering = ['-created_at']
