import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from pages.models import Category, AutoPart

def seed_data():
    # Categories
    categories = [
        "Қозғалтқыш",
        "Тежегіш жүйесі",
        "Дөңгелектер мен шиналар",
        "Автоэлектроника"
    ]

    cat_objs = {}
    for name in categories:
        cat, created = Category.objects.get_or_create(name=name)
        cat_objs[name] = cat
        print(f"Category {name} created: {created}")

    # Auto Parts
    parts = [
        {
            "name": "Поршеньдер жинағы",
            "category": cat_objs["Қозғалтқыш"],
            "price": 45000,
            "description": "Жоғары сапалы болаттан жасалған поршеньдер жинағы. Барлық заманауи қозғалтқыштарға жарамды.",
            "is_available": True,
            "is_featured": True,
            "image_url": "https://images.unsplash.com/photo-1598145673411-b998fe34b651?q=80&w=1470&auto=format&fit=crop"
        },
        {
            "name": "Тежегіш колодкалары",
            "category": cat_objs["Тежегіш жүйесі"],
            "price": 12500,
            "description": "Керамикалық тежегіш колодкалары. Ұзақ мерзімді және дыбыссыз тежеуді қамтамасыз етеді.",
            "is_available": True,
            "is_featured": True,
            "image_url": "https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?q=80&w=1632&auto=format&fit=crop"
        },
        {
            "name": "Michelin Pilot Sport 4",
            "category": cat_objs["Дөңгелектер мен шиналар"],
            "price": 85000,
            "description": "Жазғы спорттық шиналар. Жоғары басқару мүмкіндігі және жолға жақсы жабысу.",
            "is_available": True,
            "is_featured": True,
            "image_url": "https://images.unsplash.com/photo-1549147714-167375e4af4a?q=80&w=1470&auto=format&fit=crop"
        },
        {
            "name": "Автокөлік мультимедиасы",
            "category": cat_objs["Автоэлектроника"],
            "price": 120000,
            "description": "Android операциялық жүйесіндегі заманауи мультимедиалық орталық. GPS, Bluetooth, Wi-Fi қолдауы.",
            "is_available": True,
            "is_featured": True,
            "image_url": "https://images.unsplash.com/photo-1552650272-b8a34e21bc4b?q=80&w=1470&auto=format&fit=crop"
        },
        {
            "name": "Тұтандыру білтелері (Spark plugs)",
            "category": cat_objs["Қозғалтқыш"],
            "price": 3500,
            "description": "Иридий тұтандыру білтелері. Жанармай үнемдеуге және қозғалтқыштың тұрақты жұмысына көмектеседі.",
            "is_available": True,
            "is_featured": False,
            "image_url": "https://images.unsplash.com/photo-1619642751034-765dfdf7c58e?q=80&w=1374&auto=format&fit=crop"
        },
        {
            "name": "Тежегіш дискілері",
            "category": cat_objs["Тежегіш жүйесі"],
            "price": 28000,
            "description": "Жоғары температураға төзімді желдетілетін тежегіш дискілері.",
            "is_available": True,
            "is_featured": False,
            "image_url": "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?q=80&w=1470&auto=format&fit=crop"
        },
        {
            "name": "Жеңіл қорытпалы дискілер",
            "category": cat_objs["Дөңгелектер мен шиналар"],
            "price": 150000,
            "description": "R18 өлшемді жеңіл қорытпалы дискілер жинағы. Стильді дизайн және жеңіл салмақ.",
            "is_available": True,
            "is_featured": False,
            "image_url": "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?q=80&w=1470&auto=format&fit=crop"
        },
        {
            "name": "Аккумулятор 75Ah",
            "category": cat_objs["Автоэлектроника"],
            "price": 38000,
            "description": "Кез келген ауа райында сенімді іске қосуды қамтамасыз ететін жоғары қуатты аккумулятор.",
            "is_available": True,
            "is_featured": False,
            "image_url": "https://images.unsplash.com/photo-1620939511593-29937fd097e3?q=80&w=1470&auto=format&fit=crop"
        }
    ]

    for part_data in parts:
        part, created = AutoPart.objects.get_or_create(
            name=part_data["name"],
            defaults={
                "category": part_data["category"],
                "price": part_data["price"],
                "description": part_data["description"],
                "is_available": part_data["is_available"],
                "is_featured": part_data["is_featured"],
                "image_url": part_data["image_url"]
            }
        )
        print(f"Part {part.name} created: {created}")

if __name__ == "__main__":
    seed_data()
