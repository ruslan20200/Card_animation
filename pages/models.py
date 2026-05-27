from django.db import models

class JewelryCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Атауы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Зергерлік бұйым санаты"
        verbose_name_plural = "Зергерлік бұйым санаттары"
        ordering = ['name']

class JewelryItem(models.Model):
    MATERIAL_CHOICES = [
        ('Gold', 'Алтын'),
        ('Silver', 'Күміс'),
        ('Platinum', 'Платина'),
    ]

    title = models.CharField(max_length=200, verbose_name="Атауы")
    category = models.ForeignKey(JewelryCategory, on_delete=models.CASCADE, related_name='items', verbose_name="Санаты")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Бағасы")
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES, verbose_name="Материал")
    purity = models.CharField(max_length=10, verbose_name="Проба")
    description = models.TextField(verbose_name="Сипаттамасы")
    is_handcrafted = models.BooleanField(default=False, verbose_name="Қолдан жасалған")
    image_url = models.URLField(verbose_name="Сурет сілтемесі")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Зергерлік бұйым"
        verbose_name_plural = "Зергерлік бұйымдар"
        ordering = ['-id']

class JewelryOrderRequest(models.Model):
    CONTACT_METHOD_CHOICES = [
        ('Phone', 'Телефон қоңырауы'),
        ('WhatsApp', 'WhatsApp хабарламасы'),
    ]

    customer_name = models.CharField(max_length=100, verbose_name="Тапсырыс берушінің есімі")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон нөмірі")
    selected_item = models.ForeignKey(JewelryItem, on_delete=models.CASCADE, verbose_name="Таңдалған бұйым")
    preferred_size = models.CharField(max_length=20, blank=True, null=True, verbose_name="Қалаулы өлшем")
    preferred_contact_method = models.CharField(
        max_length=10,
        choices=CONTACT_METHOD_CHOICES,
        default='Phone',
        verbose_name="Байланыс тәсілі"
    )
    message = models.TextField(blank=True, null=True, verbose_name="Хабарлама")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Жасалған уақыты")

    def __str__(self):
        return f"{self.customer_name} - {self.selected_item.title}"

    class Meta:
        verbose_name = "Тапсырыс өтінімі"
        verbose_name_plural = "Тапсырыс өтінімдері"
        ordering = ['-created_at']
