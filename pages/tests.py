from django.test import TestCase
from django.urls import reverse
from .models import Currency

class PageTests(TestCase):
    def setUp(self):
        self.currency = Currency.objects.create(
            code="USD",
            name="АҚШ доллары",
            buy_rate=475.00,
            sell_rate=480.00,
            flag_url="https://flagcdn.com/w80/us.png"
        )

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_rates_page_status_code(self):
        response = self.client.get(reverse('rates'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_reserve_page_status_code(self):
        response = self.client.get(reverse('reserve'))
        self.assertEqual(response.status_code, 200)

    def test_reservation_form_submission(self):
        response = self.client.post(reverse('reserve'), {
            'client_name': 'Test User',
            'phone_number': '+77071234567',
            'source_currency': self.currency.id,
            'operation_type': 'buy',
            'amount_to_exchange': 100,
            'expected_amount': 47500
        })
        self.assertEqual(response.status_code, 302) # Redirect on success
