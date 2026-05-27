from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name="Валюта коды")
    name = models.CharField(max_length=50, verbose_name="Валюта атауы")
    buy_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сатып алу бағамы")
    sell_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сату бағамы")
    flag_url = models.URLField(verbose_name="Жалауша сілтемесі")
    is_active = models.BooleanField(default=True, verbose_name="Белсенді")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Жаңартылған уақыты")

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюталар"
        ordering = ['code']

class ExchangeReservation(models.Model):
    OPERATION_CHOICES = [
        ('buy', 'Сатып алу'),
        ('sell', 'Сату'),
    ]

    client_name = models.CharField(max_length=100, verbose_name="Клиенттің аты")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон нөмірі")
    source_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name="Валюта")
    operation_type = models.CharField(max_length=10, choices=OPERATION_CHOICES, verbose_name="Операция түрі")
    amount_to_exchange = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Айырбасталатын сома")
    expected_amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Күтілетін сома")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Құрылған уақыты")

    def __str__(self):
        return f"{self.client_name} - {self.source_currency.code} ({self.operation_type})"

    class Meta:
        verbose_name = "Валюта брондау"
        verbose_name_plural = "Валюта брондаулары"
        ordering = ['-created_at']
