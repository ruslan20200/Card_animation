from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Атауы")

    class Meta:
        verbose_name = "Санат"
        verbose_name_plural = "Санаттар"
        ordering = ['name']

    def __str__(self):
        return self.name

class BeautyService(models.Model):
    title = models.CharField(max_length=200, verbose_name="Атауы")
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name="services", verbose_name="Санат")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Бағасы (₸)")
    duration = models.CharField(max_length=50, verbose_name="Ұзақтығы")
    description = models.TextField(verbose_name="Сипаттамасы")
    image_url = models.URLField(verbose_name="Сурет URL")
    is_popular = models.BooleanField(default=False, verbose_name="Танымал ба?")

    class Meta:
        verbose_name = "Қызмет"
        verbose_name_plural = "Қызметтер"
        ordering = ['title']

    def __str__(self):
        return self.title

class Stylist(models.Model):
    name = models.CharField(max_length=100, verbose_name="Аты-жөні")
    specialty = models.CharField(max_length=100, verbose_name="Мамандығы")
    experience_years = models.PositiveIntegerField(verbose_name="Жұмыс өтілі (жыл)")
    bio = models.TextField(verbose_name="Өмірбаян", blank=True)
    photo_url = models.URLField(verbose_name="Фото URL")
    is_top = models.BooleanField(default=False, verbose_name="Үздік пе?")

    class Meta:
        verbose_name = "Шебер"
        verbose_name_plural = "Шеберлер"
        ordering = ['name']

    def __str__(self):
        return self.name

class Appointment(models.Model):
    client_name = models.CharField(max_length=100, verbose_name="Клиенттің аты-жөні")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон нөмірі")
    selected_service = models.ForeignKey(BeautyService, on_delete=models.CASCADE, verbose_name="Қызмет")
    selected_stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE, verbose_name="Шебер")
    appointment_date = models.DateField(verbose_name="Күн")
    appointment_time = models.TimeField(verbose_name="Уақыт")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Жазылған уақыты")

    class Meta:
        verbose_name = "Онлайн жазылу"
        verbose_name_plural = "Онлайн жазылулар"
        ordering = ['-appointment_date', '-appointment_time']

    def __str__(self):
        return f"{self.client_name} - {self.selected_service.title} ({self.appointment_date})"
