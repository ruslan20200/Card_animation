import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from pages.models import ServiceCategory, BeautyService, Stylist

def seed_data():
    # 1. Categories
    hair_care, _ = ServiceCategory.objects.get_or_create(name="Шаш күтімі")
    nail_service, _ = ServiceCategory.objects.get_or_create(name="Тырнақ сервисі")
    face_care, _ = ServiceCategory.objects.get_or_create(name="Бет күтімі / Визаж")

    # 2. Stylists
    stylist1, _ = Stylist.objects.get_or_create(
        name="Айгерім Сұлтанова",
        specialty="Топ-стилист",
        experience_years=8,
        bio="Шаш үлгілері мен бояу саласындағы 8 жылдық тәжірибесі бар маман. Ең күрделі бейнелерді жүзеге асырады.",
        photo_url="https://images.unsplash.com/photo-1595152772835-219674b2a8a6?q=80&w=800&auto=format&fit=crop",
        is_top=True
    )
    stylist2, _ = Stylist.objects.get_or_create(
        name="Динара Асанова",
        specialty="Тырнақ шебері",
        experience_years=5,
        bio="Мінсіз маникюр мен педикюр шебері. Дизайн мен күтімнің қыр-сырын меңгерген.",
        photo_url="https://images.unsplash.com/photo-1590650516494-0c8e4a4dd67e?q=80&w=800&auto=format&fit=crop",
        is_top=True
    )
    stylist3, _ = Stylist.objects.get_or_create(
        name="Мәдина Ибраева",
        specialty="Визажист / Косметолог",
        experience_years=6,
        bio="Сіздің табиғи сұлулығыңызды аша түсетін кәсіби макияж шебері. Бет күтімі бойынша кеңес береді.",
        photo_url="https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=800&auto=format&fit=crop",
        is_top=False
    )

    # 3. Services
    # Hair Care
    BeautyService.objects.get_or_create(
        title="Әйелдерге арналған шаш қию",
        category=hair_care,
        price=8000,
        duration="1 сағат",
        description="Кәсіби шаш қию, жуу және сәндеу кіреді. Біздің шеберлер сіздің бет пішініңізге сәйкес келетін стиль таңдап береді.",
        image_url="https://images.unsplash.com/photo-1562322140-8baeececf3df?q=80&w=800&auto=format&fit=crop",
        is_popular=True
    )
    BeautyService.objects.get_or_create(
        title="Күрделі бояу (Airtouch/Balayage)",
        category=hair_care,
        price=35000,
        duration="3-4 сағат",
        description="Шашқа зақым келтірмейтін заманауи бояу техникалары. Түстердің үйлесімді ауысуын қамтамасыз етеді.",
        image_url="https://images.unsplash.com/photo-1560869713-7d0a29430803?q=80&w=800&auto=format&fit=crop",
        is_popular=True
    )

    # Nail Service
    BeautyService.objects.get_or_create(
        title="Аппараттық маникюр + гель-лак",
        category=nail_service,
        price=7000,
        duration="1.5 сағат",
        description="Тырнақ пішінін түзету, кутикуланы тазарту және берік гель-лак жабыны. Дизайн сыйлыққа!",
        image_url="https://images.unsplash.com/photo-1604654894610-df490c81726a?q=80&w=800&auto=format&fit=crop",
        is_popular=True
    )
    BeautyService.objects.get_or_create(
        title="Smart-педикюр",
        category=nail_service,
        price=10000,
        duration="1.5 сағат",
        description="Аяқ терісіне күтім жасау және тырнақтарды сәндеу. Жаяу жүргенді ұнататындарға мінсіз таңдау.",
        image_url="https://images.unsplash.com/photo-1519014816548-bf5fe059798b?q=80&w=800&auto=format&fit=crop",
        is_popular=False
    )

    # Face Care / Makeup
    BeautyService.objects.get_or_create(
        title="Күндізгі / Кешкі макияж",
        category=face_care,
        price=12000,
        duration="1 сағат",
        description="Кез келген іс-шараға арналған мінсіз макияж. Біз тек жоғары сапалы косметиканы қолданамыз.",
        image_url="https://images.unsplash.com/photo-1512496015851-a90fb38ba796?q=80&w=800&auto=format&fit=crop",
        is_popular=True
    )
    BeautyService.objects.get_or_create(
        title="Бетті терең тазарту (пилинг)",
        category=face_care,
        price=15000,
        duration="1.5 сағат",
        description="Теріні өлі жасушалардан тазарту, ылғалдандыру және балғындық сыйлау.",
        image_url="https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?q=80&w=800&auto=format&fit=crop",
        is_popular=False
    )

    print("Деректер қоры сәтті толтырылды!")

if __name__ == "__main__":
    seed_data()
