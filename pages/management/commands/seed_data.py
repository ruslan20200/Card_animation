from django.core.management.base import BaseCommand
from pages.models import Amenity, RoomType
from django.db import transaction

class Command(BaseCommand):
    help = 'Seeds the database with initial luxury hotel data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        with transaction.atomic():
            # Clear existing data
            RoomType.objects.all().delete()
            Amenity.objects.all().delete()

            # Create Amenities
            amenities_data = [
                {'name': 'Тегін Wi-Fi', 'icon_class': 'bi-wifi'},
                {'name': 'Бассейн', 'icon_class': 'bi-water'},
                {'name': 'Таңғы ас қосылған', 'icon_class': 'bi-cup-hot'},
                {'name': 'СПА және Фитнес', 'icon_class': 'bi-heart-pulse'},
                {'name': 'Трансфер қызметі', 'icon_class': 'bi-car-front'},
                {'name': 'Мейрамхана', 'icon_class': 'bi-egg-fried'},
            ]

            amenities = {}
            for item in amenities_data:
                amenity = Amenity.objects.create(**item)
                amenities[item['name']] = amenity

            # Create Room Types
            rooms_data = [
                {
                    'name': 'Стандарт',
                    'price_per_night': 35000,
                    'capacity': 2,
                    'description': 'Жайлы әрі функционалды бөлме. Бір немесе екі қонақ үшін өте қолайлы. Заманауи жиһаздармен және қажетті жабдықтармен жабдықталған.',
                    'image_url': 'https://images.unsplash.com/photo-1566665797739-1674de7a421a?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
                    'amenities_list': ['Тегін Wi-Fi', 'Таңғы ас қосылған']
                },
                {
                    'name': 'Люкс',
                    'price_per_night': 65000,
                    'capacity': 2,
                    'description': 'Тау көрінісі бар керемет люкс бөлме. Кең қонақ бөлмесі және жайлы жатын бөлмесі бар. Премиум кластағы демалысты қалайтындар үшін.',
                    'image_url': 'https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
                    'amenities_list': ['Тегін Wi-Fi', 'Таңғы ас қосылған', 'Бассейн', 'СПА және Фитнес']
                },
                {
                    'name': 'Отбасылық бөлме',
                    'price_per_night': 85000,
                    'capacity': 4,
                    'description': 'Бүкіл отбасы үшін кең бөлме. Екі жатын бөлме және ортақ қонақ бөлмесі бар. Балалармен демалуға арналған барлық жағдай жасалған.',
                    'image_url': 'https://images.unsplash.com/photo-1591088398332-8a7791972843?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
                    'amenities_list': ['Тегін Wi-Fi', 'Таңғы ас қосылған', 'Бассейн', 'Трансфер қызметі']
                },
                {
                    'name': 'Президенттік апартамент',
                    'price_per_night': 150000,
                    'capacity': 2,
                    'description': 'Ең жоғары деңгейдегі салтанат пен жайлылық. Жеке террасасы, панорамалық тау көрінісі және эксклюзивті қызмет көрсету пакеті.',
                    'image_url': 'https://images.unsplash.com/photo-1631049307264-da0ec9d70304?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
                    'amenities_list': ['Тегін Wi-Fi', 'Таңғы ас қосылған', 'Бассейн', 'СПА және Фитнес', 'Трансфер қызметі', 'Мейрамхана']
                }
            ]

            for item in rooms_data:
                amenities_list = item.pop('amenities_list')
                room = RoomType.objects.create(**item)
                for am_name in amenities_list:
                    room.amenities.add(amenities[am_name])

        self.stdout.write(self.style.SUCCESS('Successfully seeded luxury hotel data'))
