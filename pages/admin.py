from django.contrib import admin
from .models import Amenity, RoomType, BookingRequest

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_class')

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_night', 'capacity', 'is_available')
    filter_horizontal = ('amenities',)

@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'selected_room_type', 'check_in_date', 'check_out_date', 'created_at')
    list_filter = ('selected_room_type', 'check_in_date')
    search_fields = ('guest_name', 'email', 'phone_number')
