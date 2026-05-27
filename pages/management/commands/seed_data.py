from django.core.management.base import BaseCommand
from pages.models import Author, Book

class Command(BaseCommand):
    help = 'Seeds the database with initial library data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Author.objects.all().delete()
        Book.objects.all().delete()

        # Create Authors
        a1 = Author.objects.create(
            full_name="Мұхтар Әуезов",
            bio="Мұхтар Омарханұлы Әуезов — қазақтың ұлы жазушысы, қоғам қайраткері, ғұлама ғалым, филология ғылымдарының докторы, профессор.",
            photo_url="https://images.unsplash.com/photo-1544717305-27a734ef1904?q=80&w=600"
        )
        a2 = Author.objects.create(
            full_name="Абай Құнанбаев",
            bio="Абай (Ибраһим) Құнанбайұлы — қазақтың ұлы ақыны, ағартушысы, қазақ жазба әдебиетінің, әдеби тілінің негізін қалаушы.",
            photo_url="https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=600"
        )
        a3 = Author.objects.create(
            full_name="Бауыржан Момышұлы",
            bio="Кеңес Одағының Батыры, жазушы, Екінші дүниежүзілік соғыстың даңқты жауынгері, әскери қайраткер.",
            photo_url="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=600"
        )

        # Create Books
        Book.objects.create(
            title="Абай жолы",
            author=a1,
            description="Абай жолы — Мұхтар Әуезовтің әлемге әйгілі роман-эпопеясы. Бұл шығармада қазақ халқының XIX ғасырдағы өмірі жан-жақты бейнеленген.",
            genre="Көркем әдебиет",
            publication_year=1942,
            cover_image_url="https://images.unsplash.com/photo-1544947950-fa07a98d237f?q=80&w=600"
        )
        Book.objects.create(
            title="Қара сөздер",
            author=a2,
            description="Абайдың қара сөздері — ұлы ақынның адамгершілік, имандылық, білім және ғылым туралы жазған философиялық трактаттары.",
            genre="Тұлғалық даму",
            publication_year=1890,
            cover_image_url="https://images.unsplash.com/photo-1512820790803-73c772ff376f?q=80&w=600"
        )
        Book.objects.create(
            title="Ұшқан ұя",
            author=a3,
            description="Бауыржан Момышұлының бұл шығармасында оның балалық шағы, туған жері және қазақы тәрбие туралы терең толғаныстары баяндалады.",
            genre="Көркем әдебиет",
            publication_year=1974,
            cover_image_url="https://images.unsplash.com/photo-1497633762265-9d179a990aa6?q=80&w=600"
        )
        Book.objects.create(
            title="Қазақстан тарихы",
            author=a1,
            description="Ежелгі дәуірден бүгінгі күнге дейінгі Қазақстан тарихының негізгі кезеңдерін қамтитын ғылыми еңбек.",
            genre="Тарих",
            publication_year=2010,
            cover_image_url="https://images.unsplash.com/photo-1532012197267-da84d127e765?q=80&w=600"
        )
        Book.objects.create(
            title="Өлеңдер жинағы",
            author=a2,
            description="Абайдың лирикалық өлеңдері мен поэмаларының толық жинағы. Қазақ поэзиясының інжу-маржаны.",
            genre="Поэзия",
            publication_year=1909,
            cover_image_url="https://images.unsplash.com/photo-1516979187457-637abb4f9353?q=80&w=600"
        )
        Book.objects.create(
            title="Психология негіздері",
            author=a3,
            description="Адам психологиясының қыр-сырын ашатын заманауи ғылыми зерттеулер мен әдістемелер жинағы.",
            genre="Ғылыми",
            publication_year=2021,
            cover_image_url="https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?q=80&w=600"
        )
        Book.objects.create(
            title="Мұзбалақ",
            author=a1,
            description="Табиғат пен адам арасындағы байланысты баяндайтын көркем шығарма.",
            genre="Көркем әдебиет",
            publication_year=1950,
            cover_image_url="https://images.unsplash.com/photo-1535905557558-afc4877a26fc?q=80&w=600"
        )
        Book.objects.create(
            title="Көксерек",
            author=a1,
            description="Мұхтар Әуезовтің ең танымал әңгімелерінің бірі, қасқыр мен баланың қарым-қатынасы туралы хикаят.",
            genre="Көркем әдебиет",
            publication_year=1929,
            cover_image_url="https://images.unsplash.com/photo-1589998059171-988d887df643?q=80&w=600"
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded library data.'))
