from django.contrib import admin
from .models import MedicineCategory, Medicine, OrderRequest

@admin.register(MedicineCategory)
class MedicineCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available', 'is_featured', 'requires_prescription')
    list_filter = ('category', 'is_available', 'is_featured', 'requires_prescription')
    search_fields = ('name', 'description')
    list_editable = ('price', 'is_available', 'is_featured')

@admin.register(OrderRequest)
class OrderRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone_number', 'medicine_name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('customer_name', 'phone_number', 'medicine_name')
    readonly_fields = ('created_at',)
