from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import Course, CourseCategory, Instructor, CourseEnrollment
from .forms import CourseEnrollmentForm

class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_courses'] = Course.objects.filter(is_popular=True)[:3]
        return context

class CourseListView(ListView):
    model = Course
    template_name = 'pages/course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CourseCategory.objects.all()
        context['selected_category'] = self.request.GET.get('category')
        return context

class CourseDetailView(DetailView):
    model = Course
    template_name = 'pages/course_detail.html'
    context_object_name = 'course'

class InstructorListView(ListView):
    model = Instructor
    template_name = 'pages/instructor_list.html'
    context_object_name = 'instructors'

class EnrollmentCreateView(CreateView):
    model = CourseEnrollment
    form_class = CourseEnrollmentForm
    template_name = 'pages/enrollment_form.html'
    success_url = reverse_lazy('home') # Redirect to home after success, maybe a success page later

    def get_initial(self):
        initial = super().get_initial()
        course_id = self.request.GET.get('course')
        if course_id:
            initial['selected_course'] = get_object_or_404(Course, pk=course_id)
        return initial

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class ContactView(TemplateView):
    template_name = 'pages/contact.html'
