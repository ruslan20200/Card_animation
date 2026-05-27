from django.core.management.base import BaseCommand
from pages.models import CourseCategory, Instructor, Course

class Command(BaseCommand):
    help = 'Seeds the database with initial educational data'

    def handle(self, *args, **options):
        # Clear existing data
        Course.objects.all().delete()
        Instructor.objects.all().delete()
        CourseCategory.objects.all().delete()

        # Create Categories
        it_cat = CourseCategory.objects.create(name="Бағдарламалау (IT)")
        lang_cat = CourseCategory.objects.create(name="Тіл үйрену")
        business_cat = CourseCategory.objects.create(name="Бизнес және Маркетинг")

        # Create Instructors
        inst1 = Instructor.objects.create(
            name="Арман Серіков",
            specialty="Senior Fullstack Developer",
            bio="10 жылдық тәжірибесі бар маман. Google және Amazon компанияларында жұмыс істеген.",
            photo_url="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80"
        )
        inst2 = Instructor.objects.create(
            name="Айгүл Мұратқызы",
            specialty="Ағылшын тілі маманы (IELTS 8.5)",
            bio="Кембридж университетінің түлегі. 7 жылдық оқытушылық тәжірибесі бар.",
            photo_url="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80"
        )
        inst3 = Instructor.objects.create(
            name="Данияр Ахметов",
            specialty="Маркетинг және Стратегия",
            bio="Көптеген халықаралық брендтердің маркетингтік стратегиясын құрған сарапшы.",
            photo_url="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80"
        )

        # Create Courses
        Course.objects.create(
            title="Python бағдарламалау негіздері",
            category=it_cat,
            instructor=inst1,
            description="Нөлден бастап Python тілін үйреніңіз. Алгоритмдер, деректер құрылымы және веб-әзірлеу негіздері.",
            duration="3 ай",
            price=45000,
            is_popular=True,
            image_url="https://images.unsplash.com/photo-1515879218367-8466d910aaa4?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            level="Бастаушы",
            start_date="Маусым 2026"
        )
        Course.objects.create(
            title="React.js арқылы заманауи интерфейстер",
            category=it_cat,
            instructor=inst1,
            description="Күрделі веб-қосымшаларды жасауды үйреніңіз. State management, Hooks және API-мен жұмыс.",
            duration="4 ай",
            price=60000,
            is_popular=True,
            image_url="https://images.unsplash.com/photo-1633356122544-f134324a6cee?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            level="Жетілдірілген",
            start_date="Шілде 2026"
        )
        Course.objects.create(
            title="IELTS-ке қарқынды дайындық",
            category=lang_cat,
            instructor=inst2,
            description="IELTS емтиханының барлық бөлімдері бойынша тереңдетілген дайындық. Reading, Listening, Writing, Speaking.",
            duration="2 ай",
            price=35000,
            is_popular=True,
            image_url="https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            level="Жетілдірілген",
            start_date="Маусым 2026"
        )
        Course.objects.create(
            title="Іскерлік ағылшын тілі",
            category=lang_cat,
            instructor=inst2,
            description="Жұмыс пен бизнеске арналған ағылшын тілі. Презентация жасау, хат алмасу және келіссөздер жүргізу.",
            duration="3 ай",
            price=40000,
            is_popular=False,
            image_url="https://images.unsplash.com/photo-1543269865-cbf427effbad?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            level="Орташа",
            start_date="Тамыз 2026"
        )
        Course.objects.create(
            title="Цифрлық маркетинг стратегиясы",
            category=business_cat,
            instructor=inst3,
            description="SMM, Target, SEO және контекстік жарнама арқылы сатылымды арттыру жолдары.",
            duration="3 ай",
            price=50000,
            is_popular=True,
            image_url="https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            level="Бастаушы",
            start_date="Маусым 2026"
        )
        Course.objects.create(
            title="Стартапты нөлден бастау",
            category=business_cat,
            instructor=inst3,
            description="Идеядан алғашқы сатылымға дейін. Бизнес-модель құру, инвестиция тарту және команда жинау.",
            duration="4 ай",
            price=70000,
            is_popular=False,
            image_url="https://images.unsplash.com/photo-1519389950473-47ba0277781c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            level="Жетілдірілген",
            start_date="Қыркүйек 2026"
        )

        self.stdout.write(self.style.SUCCESS('Database successfully seeded with educational data!'))
