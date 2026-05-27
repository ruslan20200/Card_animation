from django.test import TestCase
from django.urls import reverse
from .models import AgeGroup, Teacher, EnrollmentRequest

class KindergartenTests(TestCase):
    def setUp(self):
        self.group = AgeGroup.objects.create(
            name="Test Group",
            age_range="2-3 жас",
            monthly_price=40000,
            description="Test Description",
            capacity=10,
            image_url="http://example.com/image.jpg"
        )
        self.teacher = Teacher.objects.create(
            full_name="Test Teacher",
            specialty="Test Specialty",
            experience_years=5,
            biography="Test Bio",
            photo_url="http://example.com/photo.jpg"
        )

    def test_homepage_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_group_list_status_code(self):
        response = self.client.get(reverse('group_list'))
        self.assertEqual(response.status_code, 200)

    def test_teacher_list_status_code(self):
        response = self.client.get(reverse('teacher_list'))
        self.assertEqual(response.status_code, 200)

    def test_enrollment_form_status_code(self):
        response = self.client.get(reverse('enroll'))
        self.assertEqual(response.status_code, 200)

    def test_about_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_enrollment_submission(self):
        response = self.client.post(reverse('enroll'), {
            'parent_name': 'Parent Name',
            'phone_number': '+77012345678',
            'child_name': 'Child Name',
            'child_age': 3,
            'selected_group': self.group.id,
            'message': 'Test Message'
        })
        self.assertRedirects(response, reverse('thanks'))
        self.assertEqual(EnrollmentRequest.objects.count(), 1)
