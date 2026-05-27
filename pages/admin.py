from django.contrib import admin
from .models import Category, AutoPart, ContactMessage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(AutoPart)
class AutoPartAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "is_available", "is_featured")
    list_filter = ("category", "is_available", "is_featured")
    search_fields = ("name", "description")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    readonly_fields = ("name", "email", "subject", "message", "created_at")
    search_fields = ("name", "email", "subject")
