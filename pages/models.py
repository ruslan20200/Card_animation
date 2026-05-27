from django.db import models

class CourseCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Санат атауы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс санаты"
        verbose_name_plural = "Курс санаттары"
        ordering = ['name']

class Instructor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Аты-жөні")
    specialty = models.CharField(max_length=100, verbose_name="Мамандығы")
    bio = models.TextField(verbose_name="Өмірбаян")
    photo_url = models.URLField(verbose_name="Фото URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Оқытушы"
        verbose_name_plural = "Оқытушылар"
        ordering = ['name']

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Курс атауы")
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='courses', verbose_name="Санат")
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses', verbose_name="Оқытушы")
    description = models.TextField(verbose_name="Сипаттама")
    duration = models.CharField(max_length=50, verbose_name="Ұзақтығы")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Бағасы")
    is_popular = models.BooleanField(default=False, verbose_name="Танымал")
    image_url = models.URLField(verbose_name="Сурет URL")
    level = models.CharField(max_length=50, verbose_name="Деңгейі")
    start_date = models.CharField(max_length=50, verbose_name="Басталуы")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курстар"
        ordering = ['title']

class CourseEnrollment(models.Model):
    student_name = models.CharField(max_length=100, verbose_name="Студенттің аты-жөні")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон нөмірі")
    email = models.EmailField(verbose_name="Электрондық пошта")
    selected_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Таңдалған курс")
    message = models.TextField(blank=True, verbose_name="Хабарлама")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Құрылған уақыты")

    def __str__(self):
        return f"{self.student_name} - {self.selected_course.title}"

    class Meta:
        verbose_name = "Курсқа жазылу"
        verbose_name_plural = "Курсқа жазылулар"
        ordering = ['-created_at']
