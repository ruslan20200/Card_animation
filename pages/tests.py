from django.test import TestCase
from django.urls import reverse
from .models import ProductCategory, Product

class GroceryStoreTests(TestCase):
    def setUp(self):
        self.category = ProductCategory.objects.create(name="Жемістер")
        self.product = Product.objects.create(
            title="Алма",
            category=self.category,
            price=500,
            weight_info="1 кг",
            image_url="https://example.com/image.jpg",
            is_on_sale=True
        )

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_catalog_page_status_code(self):
        response = self.client.get(reverse('catalog'))
        self.assertEqual(response.status_code, 200)

    def test_order_page_status_code(self):
        response = self.client.get(reverse('order_create'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_order_prefill(self):
        response = self.client.get(reverse('order_create') + f"?product={self.product.id}")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'value="{self.product.id}" selected')

    def test_invalid_quantity(self):
        response = self.client.post(reverse('order_create'), {
            'customer_name': 'Тест',
            'phone_number': '123',
            'delivery_address': 'Мекенжай',
            'selected_product': self.product.id,
            'quantity': 51
        })
        self.assertFormError(response, 'form', 'quantity', "Бір тапсырыста 50-ден көп тауар алуға болмайды.")

    def assertFormError(self, response, form_name, field_name, error_msg):
        # Helper to handle the case where response context might not have the form directly in the way expected by older assertFormError
        form = response.context[form_name]
        self.assertIn(error_msg, form.errors.get(field_name, []))
