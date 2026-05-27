import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from pages.models import Medicine, MedicineCategory

def seed_data():
    # Clear existing data
    Medicine.objects.all().delete()
    MedicineCategory.objects.all().delete()

    # Categories
    vitamins = MedicineCategory.objects.create(name="Витаминдер")
    painkillers = MedicineCategory.objects.create(name="Ауыруды басатын дәрілер")
    antibiotics = MedicineCategory.objects.create(name="Антибиотиктер")
    first_aid = MedicineCategory.objects.create(name="Алғашқы көмек")

    # Medicines
    medicines = [
        {
            "name": "Мультивитаминді кешен",
            "category": vitamins,
            "price": 4500,
            "description": "Күнделікті қолдануға арналған дәрумендер жиынтығы.",
            "requires_prescription": False,
            "is_available": True,
            "is_featured": True,
            "image_url": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "Парацетамол",
            "category": painkillers,
            "price": 150,
            "description": "Дене қызуын түсіретін және ауырсынуды басатын дәрі.",
            "requires_prescription": False,
            "is_available": True,
            "is_featured": True,
            "image_url": "https://images.unsplash.com/photo-1550572017-ed20bb7f71e2?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "Амоксициллин",
            "category": antibiotics,
            "price": 2800,
            "description": "Кең ауқымды антибиотик. Тек дәрігердің нұсқауымен қолданыңыз.",
            "requires_prescription": True,
            "is_available": True,
            "is_featured": False,
            "image_url": "https://images.unsplash.com/photo-1471864190281-ad5fe9bb0724?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "С витамині",
            "category": vitamins,
            "price": 800,
            "description": "Иммунитетті нығайтуға арналған аскорбин қышқылы.",
            "requires_prescription": False,
            "is_available": True,
            "is_featured": True,
            "image_url": "https://images.unsplash.com/photo-1616671285442-45e0f77977a4?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "Ибупрофен",
            "category": painkillers,
            "price": 600,
            "description": "Қабынуға қарсы және ауырсынуды басатын құрал.",
            "requires_prescription": False,
            "is_available": True,
            "is_featured": False,
            "image_url": "https://images.unsplash.com/photo-1584017911766-d451b3d0e843?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "Алғашқы көмек қобдишасы",
            "category": first_aid,
            "price": 12000,
            "description": "Үйге немесе көлікке арналған толық жиынтық.",
            "requires_prescription": False,
            "is_available": True,
            "is_featured": True,
            "image_url": "https://images.unsplash.com/photo-1603398938378-e54eab446f8a?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "Цефтриаксон",
            "category": antibiotics,
            "price": 3500,
            "description": "Күшті әсер ететін инъекциялық антибиотик.",
            "requires_prescription": True,
            "is_available": True,
            "is_featured": False,
            "image_url": "https://images.unsplash.com/photo-1587854680352-936b22b91030?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "name": "Магний B6",
            "category": vitamins,
            "price": 3200,
            "description": "Жүйке жүйесін нығайтуға арналған препарат.",
            "requires_prescription": False,
            "is_available": True,
            "is_featured": False,
            "image_url": "https://images.unsplash.com/photo-1626785774573-4b799315345d?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        }
    ]

    for med_data in medicines:
        Medicine.objects.create(**med_data)

    print(f"Successfully seeded {len(medicines)} medicines and 4 categories.")

if __name__ == "__main__":
    seed_data()
