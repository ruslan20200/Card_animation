from django.test import TestCase
from django.urls import reverse
from .models import Medicine, MedicineCategory

class PharmacyPagesTests(TestCase):
    def setUp(self):
        self.category = MedicineCategory.objects.create(name="Тест Категория")
        self.medicine = Medicine.objects.create(
            name="Тест Дәрі",
            category=self.category,
            price=1000,
            description="Тест сипаттама",
            image_url="http://example.com/image.jpg",
            is_featured=True
        )

    def test_homepage_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_catalog_page_status_code(self):
        response = self.client.get(reverse('catalog'))
        self.assertEqual(response.status_code, 200)

    def test_medicine_detail_page_status_code(self):
        response = self.client.get(reverse('medicine_detail', kwargs={'pk': self.medicine.pk}))
        self.assertEqual(response.status_code, 200)

    def test_order_form_page_status_code(self):
        response = self.client.get(reverse('order_form'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Денсаулық — басты байлық")
        self.assertContains(response, "Басты бет")
        self.assertContains(response, "Тест Дәрі")
