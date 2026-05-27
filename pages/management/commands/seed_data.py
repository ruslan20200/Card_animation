from django.core.management.base import BaseCommand
from pages.models import Currency

class Command(BaseCommand):
    help = 'Seed the database with initial currencies'

    def handle(self, *args, **options):
        currencies = [
            {
                'code': 'USD',
                'name': 'АҚШ доллары',
                'buy_rate': 475.50,
                'sell_rate': 480.20,
                'flag_url': 'https://flagcdn.com/w80/us.png'
            },
            {
                'code': 'EUR',
                'name': 'Еуро',
                'buy_rate': 515.00,
                'sell_rate': 522.50,
                'flag_url': 'https://flagcdn.com/w80/eu.png'
            },
            {
                'code': 'RUB',
                'name': 'Ресей рублі',
                'buy_rate': 5.10,
                'sell_rate': 5.45,
                'flag_url': 'https://flagcdn.com/w80/ru.png'
            },
            {
                'code': 'CNY',
                'name': 'Қытай юані',
                'buy_rate': 65.20,
                'sell_rate': 67.80,
                'flag_url': 'https://flagcdn.com/w80/cn.png'
            },
        ]

        for curr_data in currencies:
            currency, created = Currency.objects.update_or_create(
                code=curr_data['code'],
                defaults=curr_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Валюта {currency.code} қосылды"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Валюта {currency.code} жаңартылды"))
