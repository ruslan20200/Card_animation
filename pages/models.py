from django.db import models

class Amenity(models.Model):
    name = models.CharField(max_length=100, verbose_name="Атауы")
    icon_class = models.CharField(max_length=50, verbose_name="Иконка классы")

    class Meta:
        verbose_name = "Ыңғайлылық"
        verbose_name_plural = "Ыңғайлылықтар"
        ordering = ['name']

    def __str__(self):
        return self.name

class RoomType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Бөлме түрі")
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Тәулігіне бағасы")
    capacity = models.PositiveIntegerField(verbose_name="Сыйымдылығы (адам саны)")
    description = models.TextField(verbose_name="Сипаттамасы")
    image_url = models.URLField(verbose_name="Сурет сілтемесі")
    is_available = models.BooleanField(default=True, verbose_name="Қолжетімді")
    amenities = models.ManyToManyField(Amenity, related_name="rooms", verbose_name="Ыңғайлылықтар")

    class Meta:
        verbose_name = "Бөлме түрі"
        verbose_name_plural = "Бөлмелер түрлері"
        ordering = ['price_per_night']

    def __str__(self):
        return self.name

class BookingRequest(models.Model):
    guest_name = models.CharField(max_length=100, verbose_name="Қонақтың аты-жөні")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон нөмірі")
    email = models.EmailField(verbose_name="Электронды пошта")
    selected_room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, verbose_name="Таңдалған бөлме түрі")
    check_in_date = models.DateField(verbose_name="Келу күні")
    check_out_date = models.DateField(verbose_name="Кету күні")
    guest_count = models.PositiveIntegerField(verbose_name="Қонақтар саны")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Құрылған уақыты")

    class Meta:
        verbose_name = "Брондау өтінімі"
        verbose_name_plural = "Брондау өтінімдері"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.guest_name} - {self.selected_room_type.name}"
