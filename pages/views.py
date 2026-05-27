from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, CreateView
from django.urls import reverse_lazy
from .models import AgeGroup, Teacher, EnrollmentRequest
from .forms import EnrollmentForm

def home(request):
    featured_groups = AgeGroup.objects.all()[:3]
    return render(request, 'home.html', {'featured_groups': featured_groups})

class GroupListView(ListView):
    model = AgeGroup
    template_name = 'pages/group_list.html'
    context_object_name = 'groups'

    def get_queryset(self):
        queryset = super().get_queryset()
        age_range = self.request.GET.get('age_range')
        if age_range:
            queryset = queryset.filter(age_range__icontains=age_range)
        return queryset

class TeacherListView(ListView):
    model = Teacher
    template_name = 'pages/teacher_list.html'
    context_object_name = 'teachers'

class EnrollmentCreateView(CreateView):
    model = EnrollmentRequest
    form_class = EnrollmentForm
    template_name = 'pages/enrollment_form.html'
    success_url = reverse_lazy('thanks')

class ThanksTemplateView(TemplateView):
    template_name = 'pages/thanks.html'

class AboutTemplateView(TemplateView):
    template_name = 'pages/about.html'
