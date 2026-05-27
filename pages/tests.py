from django.test import TestCase
from django.urls import reverse
from .models import RoomType, Amenity

class HotelTests(TestCase):
    def setUp(self):
        self.amenity = Amenity.objects.create(name="Wifi", icon_class="bi-wifi")
        self.room = RoomType.objects.create(
            name="Test Room",
            price_per_night=50000,
            capacity=2,
            description="Test Description",
            image_url="http://example.com/image.jpg"
        )
        self.room.amenities.add(self.amenity)

    def test_pages_accessibility(self):
        pages = ['home', 'room_catalog', 'about', 'contact', 'booking_form']
        for page in pages:
            response = self.client.get(reverse(page))
            self.assertEqual(response.status_code, 200)

    def test_room_detail_accessibility(self):
        response = self.client.get(reverse('room_detail', args=[self.room.pk]))
        self.assertEqual(response.status_code, 200)

    def test_booking_validation(self):
        data = {
            'guest_name': 'Test Guest',
            'phone_number': '123456789',
            'email': 'test@example.com',
            'selected_room_type': self.room.pk,
            'check_in_date': '2024-12-10',
            'check_out_date': '2024-12-05', # Invalid
            'guest_count': 2
        }
        response = self.client.post(reverse('booking_form'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Кету күні келу күнінен кешірек болуы керек.")
