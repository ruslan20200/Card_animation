from django.core.management.base import BaseCommand
from pages.models import AgeGroup, Teacher

class Command(BaseCommand):
    help = 'Seeds the database with kindergarten mock data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        AgeGroup.objects.all().delete()
        Teacher.objects.all().delete()

        # Seed Age Groups
        groups_data = [
            {
                "name": "«Құлыншақ» кіші тобы",
                "age_range": "2-3 жас",
                "monthly_price": 45000,
                "description": "Балалардың алғашқы әлеуметтік дағдыларын қалыптастыруға арналған жайлы орта. Ойын арқылы даму және қамқорлық.",
                "capacity": 15,
                "image_url": "https://images.unsplash.com/photo-1587654780291-39c9404d746b?q=80&w=1000"
            },
            {
                "name": "«Балдырған» орта тобы",
                "age_range": "3-4 жас",
                "monthly_price": 50000,
                "description": "Шығармашылық пен танымдық белсенділікті арттыру. Тіл дамыту және қоршаған ортамен танысу сабақтары.",
                "capacity": 20,
                "image_url": "https://images.unsplash.com/photo-1596464716127-f2a82984de30?q=80&w=1000"
            },
            {
                "name": "«Тұлпар» ересек тобы",
                "age_range": "4-5 жас",
                "monthly_price": 55000,
                "description": "Мектепке дейінгі дайындық элементтері. Логикалық ойлау, математика негіздері және ағылшын тілі.",
                "capacity": 20,
                "image_url": "https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?q=80&w=1000"
            },
            {
                "name": "«Болашақ» мектепалды тобы",
                "age_range": "5-6 жас",
                "monthly_price": 60000,
                "description": "Мектепке толыққанды дайындық. Оқу, жазу және психологиялық бейімделу бағдарламалары.",
                "capacity": 25,
                "image_url": "https://images.unsplash.com/photo-1516627145497-ae6968895b74?q=80&w=1000"
            }
        ]

        for item in groups_data:
            AgeGroup.objects.create(**item)

        # Seed Teachers
        teachers_data = [
            {
                "full_name": "Әлия Серікқызы",
                "specialty": "Бас тәрбиеші",
                "experience_years": 12,
                "biography": "Жоғары санатты педагог. Балалар психологиясы мен тәрбиесі саласында 10 жылдан астам тәжірибесі бар.",
                "photo_url": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=1000"
            },
            {
                "full_name": "Марат Асқарұлы",
                "specialty": "Музыка мұғалімі",
                "experience_years": 8,
                "biography": "Балаларға музыка әлемін ашып, олардың вокалдық және аспаптық қабілеттерін дамытады.",
                "photo_url": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?q=80&w=1000"
            },
            {
                "full_name": "Гүлнар Бақытжанқызы",
                "specialty": "Ағылшын тілі маманы",
                "experience_years": 5,
                "biography": "Ойын түріндегі ағылшын тілі сабақтары арқылы балалардың тілге деген қызығушылығын оятады.",
                "photo_url": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=1000"
            },
            {
                "full_name": "Айгерім Дәуренқызы",
                "specialty": "Логопед-дефектолог",
                "experience_years": 7,
                "biography": "Сөйлеу мәдениетін қалыптастыру және тіл кемістіктерін түзету бойынша білікті маман.",
                "photo_url": "https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=1000"
            }
        ]

        for item in teachers_data:
            Teacher.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Successfully seeded kindergarten data'))
