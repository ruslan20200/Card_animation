from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Санат атауы")

    class Meta:
        verbose_name = "Өнім санаты"
        verbose_name_plural = "Өнім санаттары"
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Атауы")
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products', verbose_name="Санаты")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Бағасы (тг)")
    weight_info = models.CharField(max_length=50, verbose_name="Салмағы/Көлемі", help_text="Мысалы: 1 кг, 500 г, 1 л")
    description = models.TextField(verbose_name="Сипаттамасы", blank=True)
    is_fresh = models.BooleanField(default=False, verbose_name="Балғын өнім")
    is_on_sale = models.BooleanField(default=False, verbose_name="Жеңілдік")
    image_url = models.URLField(verbose_name="Сурет сілтемесі")

    class Meta:
        verbose_name = "Өнім"
        verbose_name_plural = "Өнімдер"
        ordering = ['title']

    def __str__(self):
        return self.title

class DeliveryRequest(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name="Тапсырыс берушінің аты-жөні")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон нөмірі")
    delivery_address = models.TextField(verbose_name="Жеткізу мекенжайы")
    selected_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Таңдалған өнім")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Саны")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Құрылған уақыты")

    class Meta:
        verbose_name = "Тапсырыс"
        verbose_name_plural = "Тапсырыстар"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.customer_name} - {self.selected_product.title}"
