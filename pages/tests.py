from django.test import TestCase
from django.urls import reverse
from .models import Category, AutoPart

class AutoPartTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Тест санаты")
        self.part = AutoPart.objects.create(
            name="Тест бөлшек",
            category=self.category,
            price=1000,
            description="Тест сипаттамасы",
            is_available=True,
            is_featured=True,
            image_url="http://example.com/image.jpg"
        )

    def test_home_page_status_code(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_catalog_page_status_code(self):
        response = self.client.get(reverse("catalog"))
        self.assertEqual(response.status_code, 200)

    def test_part_detail_page_status_code(self):
        response = self.client.get(reverse("part_detail", args=[self.part.id]))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_featured_part_in_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, self.part.name)

    def test_catalog_filtering(self):
        new_category = Category.objects.create(name="Басқа санат")
        response = self.client.get(reverse("catalog") + f"?category={new_category.id}")
        self.assertNotContains(response, self.part.name)
