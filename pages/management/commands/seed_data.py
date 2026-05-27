from django.core.management.base import BaseCommand
from pages.models import ProductCategory, Product

class Command(BaseCommand):
    help = 'Seed the database with initial grocery data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Product.objects.all().delete()
        ProductCategory.objects.all().delete()

        # Create Categories
        cats = {
            'fruits_veg': ProductCategory.objects.create(name="Жемістер мен көкөністер"),
            'dairy': ProductCategory.objects.create(name="Сүт өнімдері"),
            'bakery': ProductCategory.objects.create(name="Наубайхана"),
        }

        # Create Products
        products = [
            {
                'title': "Қызыл алма",
                'category': cats['fruits_veg'],
                'price': 650.00,
                'weight_info': "1 кг",
                'description': "Тәтті әрі қытырлақ қызыл алмалар. Дәрумендерге бай.",
                'is_fresh': True,
                'is_on_sale': False,
                'image_url': "https://images.unsplash.com/photo-1560806887-1e4cd0b6bcd6?auto=format&fit=crop&w=800&q=80"
            },
            {
                'title': "Банан",
                'category': cats['fruits_veg'],
                'price': 800.00,
                'weight_info': "1 кг",
                'description': "Эквадордан әкелінген балғын банандар.",
                'is_fresh': False,
                'is_on_sale': True,
                'image_url': "https://images.unsplash.com/photo-1571771894821-ad99024177c6?auto=format&fit=crop&w=800&q=80"
            },
            {
                'title': "Сүт 3.2%",
                'category': cats['dairy'],
                'price': 450.00,
                'weight_info': "1 л",
                'description': "Табиғи сиыр сүті, пастерленген.",
                'is_fresh': True,
                'is_on_sale': False,
                'image_url': "https://images.unsplash.com/photo-1563636619-e9107da5a1bb?auto=format&fit=crop&w=800&q=80"
            },
            {
                'title': "Ірімшік (Творог)",
                'category': cats['dairy'],
                'price': 1200.00,
                'weight_info': "500 г",
                'description': "Үй ірімшігі, майлылығы 9%.",
                'is_fresh': True,
                'is_on_sale': False,
                'image_url': "https://images.unsplash.com/photo-1559561853-08451507cbe7?auto=format&fit=crop&w=800&q=80"
            },
            {
                'title': "Бауырсақ",
                'category': cats['bakery'],
                'price': 900.00,
                'weight_info': "1 кг",
                'description': "Ыстық, жұмсақ әрі дәмді бауырсақтар.",
                'is_fresh': True,
                'is_on_sale': True,
                'image_url': "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80"
            },
            {
                'title': "Қара бидай наны",
                'category': cats['bakery'],
                'price': 180.00,
                'weight_info': "400 г",
                'description': "Дәрумендерге бай қара бидай наны.",
                'is_fresh': False,
                'is_on_sale': False,
                'image_url': "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80"
            },
            {
                'title': "Қияр",
                'category': cats['fruits_veg'],
                'price': 550.00,
                'weight_info': "1 кг",
                'description': "Жергілікті жылыжайдан алынған балғын қиярлар.",
                'is_fresh': True,
                'is_on_sale': False,
                'image_url': "https://images.unsplash.com/photo-1449333254714-22e3087bc5c2?auto=format&fit=crop&w=800&q=80"
            },
            {
                'title': "Қаймақ",
                'category': cats['dairy'],
                'price': 600.00,
                'weight_info': "400 г",
                'description': "Қою әрі дәмді қаймақ, 20%.",
                'is_fresh': True,
                'is_on_sale': False,
                'image_url': "https://images.unsplash.com/photo-1528750951163-f014fc951ac7?auto=format&fit=crop&w=800&q=80"
            },
        ]

        for p_data in products:
            Product.objects.create(**p_data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded grocery data'))
