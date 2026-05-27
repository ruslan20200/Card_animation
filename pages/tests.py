from django.test import TestCase
from django.urls import reverse
from .models import JewelryCategory, JewelryItem

class JewelryStoreTests(TestCase):
    def setUp(self):
        self.category = JewelryCategory.objects.create(name="Тест санаты")
        self.item = JewelryItem.objects.create(
            title="Тест бұйым",
            category=self.category,
            price=1000,
            material="Gold",
            purity="585",
            description="Тест сипаттамасы",
            image_url="http://example.com/image.jpg"
        )

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_catalog_page_status_code(self):
        response = self.client.get(reverse('catalog'))
        self.assertEqual(response.status_code, 200)

    def test_order_page_status_code(self):
        response = self.client.get(reverse('order'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
