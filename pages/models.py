from django.db import models

class AgeGroup(models.Model):
    name = models.CharField(max_length=100, verbose_name="Топ атауы")
    age_range = models.CharField(max_length=50, verbose_name="Жас аралығы")
    monthly_price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Айлық төлем (₸)")
    description = models.TextField(verbose_name="Сипаттамасы")
    capacity = models.PositiveIntegerField(verbose_name="Сыйымдылығы")
    image_url = models.URLField(verbose_name="Сурет сілтемесі")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жас тобы"
        verbose_name_plural = "Жас топтары"
        ordering = ['name']

class Teacher(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Толық аты-жөні")
    specialty = models.CharField(max_length=100, verbose_name="Мамандығы")
    experience_years = models.PositiveIntegerField(verbose_name="Жұмыс өтілі (жыл)")
    biography = models.TextField(verbose_name="Өмірбаяны")
    photo_url = models.URLField(verbose_name="Фото сілтемесі")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Тәрбиеші"
        verbose_name_plural = "Тәрбиешілер"
        ordering = ['full_name']

class EnrollmentRequest(models.Model):
    parent_name = models.CharField(max_length=200, verbose_name="Ата-ананың аты-жөні")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон нөмірі")
    child_name = models.CharField(max_length=200, verbose_name="Баланың аты-жөні")
    child_age = models.PositiveIntegerField(verbose_name="Баланың жасы")
    selected_group = models.ForeignKey(AgeGroup, on_delete=models.SET_NULL, null=True, verbose_name="Таңдалған топ")
    message = models.TextField(blank=True, verbose_name="Хабарлама")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Құрылған уақыты")

    def __str__(self):
        return f"{self.child_name} үшін өтінім"

    class Meta:
        verbose_name = "Қабылдауға өтінім"
        verbose_name_plural = "Қабылдауға өтінімдер"
        ordering = ['-created_at']
