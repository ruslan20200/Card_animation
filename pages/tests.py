from django.test import TestCase
from django.urls import reverse
from .models import ServiceCategory, BeautyService, Stylist

class SalonPagesTests(TestCase):
    def setUp(self):
        self.category = ServiceCategory.objects.create(name="Тест Санат")
        self.service = BeautyService.objects.create(
            title="Тест Қызмет",
            category=self.category,
            price=5000,
            duration="30 мин",
            description="Тест сипаттама",
            image_url="http://example.com/image.jpg"
        )
        self.stylist = Stylist.objects.create(
            name="Тест Шебер",
            specialty="Тест Мамандығы",
            experience_years=5,
            photo_url="http://example.com/photo.jpg"
        )

    def test_homepage_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_catalog_page_status_code(self):
        response = self.client.get(reverse('catalog'))
        self.assertEqual(response.status_code, 200)

    def test_stylists_page_status_code(self):
        response = self.client.get(reverse('stylists'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_appointment_page_status_code(self):
        response = self.client.get(reverse('appointment'))
        self.assertEqual(response.status_code, 200)

    def test_appointment_preselection(self):
        response = self.client.get(reverse('appointment'), {'service': self.service.id, 'stylist': self.stylist.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.service.title)
        self.assertContains(response, self.stylist.name)
