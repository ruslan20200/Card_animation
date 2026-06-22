from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('groups/', views.GroupListView.as_view(), name='group_list'),
    path('teachers/', views.TeacherListView.as_view(), name='teacher_list'),
    path('enroll/', views.EnrollmentCreateView.as_view(), name='enroll'),
    path('thanks/', views.ThanksTemplateView.as_view(), name='thanks'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
]
