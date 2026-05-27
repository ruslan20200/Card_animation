from django.contrib import admin
from .models import ProductCategory, Product, DeliveryRequest

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'is_fresh', 'is_on_sale')
    list_filter = ('category', 'is_fresh', 'is_on_sale')
    search_fields = ('title', 'description')

@admin.register(DeliveryRequest)
class DeliveryRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone_number', 'selected_product', 'quantity', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('customer_name', 'phone_number', 'delivery_address')
