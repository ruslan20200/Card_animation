from django.urls import path
from .views import (
    HomeView,
    CourseListView,
    CourseDetailView,
    InstructorListView,
    EnrollmentCreateView,
    AboutView,
    ContactView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('instructors/', InstructorListView.as_view(), name='instructor_list'),
    path('enroll/', EnrollmentCreateView.as_view(), name='enroll'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
