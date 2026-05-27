from django.test import TestCase
from django.urls import reverse
from .models import Course, CourseCategory, Instructor

class PageAccessTest(TestCase):
    def setUp(self):
        self.category = CourseCategory.objects.create(name="Test Category")
        self.instructor = Instructor.objects.create(
            name="Test Instructor",
            specialty="Test Specialty",
            bio="Test Bio",
            photo_url="http://example.com/photo.jpg"
        )
        self.course = Course.objects.create(
            title="Test Course",
            category=self.category,
            instructor=self.instructor,
            description="Test Description",
            duration="1 month",
            price=1000,
            image_url="http://example.com/image.jpg",
            level="Beginner",
            start_date="June 2026"
        )

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_course_list_page_status_code(self):
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, 200)

    def test_course_detail_page_status_code(self):
        response = self.client.get(reverse('course_detail', args=[self.course.id]))
        self.assertEqual(response.status_code, 200)

    def test_instructor_list_page_status_code(self):
        response = self.client.get(reverse('instructor_list'))
        self.assertEqual(response.status_code, 200)

    def test_enrollment_page_status_code(self):
        response = self.client.get(reverse('enroll'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
