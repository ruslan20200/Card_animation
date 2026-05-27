from django.contrib import admin
from .models import JewelryCategory, JewelryItem, JewelryOrderRequest

@admin.register(JewelryCategory)
class JewelryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(JewelryItem)
class JewelryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'material', 'purity', 'is_handcrafted')
    list_filter = ('category', 'material', 'is_handcrafted')
    search_fields = ('title', 'description')

@admin.register(JewelryOrderRequest)
class JewelryOrderRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone_number', 'selected_item', 'preferred_contact_method', 'created_at')
    list_filter = ('preferred_contact_method', 'created_at')
    search_fields = ('customer_name', 'phone_number', 'message')
