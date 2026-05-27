from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import RoomType, Amenity, BookingRequest
from .forms import BookingForm

class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_rooms'] = RoomType.objects.filter(is_available=True)[:3]
        context['amenities'] = Amenity.objects.all()[:6]
        return context

class RoomCatalogView(ListView):
    model = RoomType
    template_name = "pages/room_catalog.html"
    context_object_name = "rooms"

    def get_queryset(self):
        queryset = RoomType.objects.filter(is_available=True)
        capacity = self.request.GET.get('capacity')
        price_tier = self.request.GET.get('tier')

        if capacity:
            queryset = queryset.filter(capacity__gte=capacity)

        if price_tier:
            if price_tier == 'economy':
                queryset = queryset.filter(price_per_night__lt=50000)
            elif price_tier == 'luxury':
                queryset = queryset.filter(price_per_night__gte=50000)

        return queryset

class RoomDetailView(DetailView):
    model = RoomType
    template_name = "pages/room_detail.html"
    context_object_name = "room"

class BookingCreateView(CreateView):
    model = BookingRequest
    form_class = BookingForm
    template_name = "pages/booking_form.html"
    success_url = reverse_lazy('booking_success')

    def get_initial(self):
        initial = super().get_initial()
        room_id = self.request.GET.get('room')
        if room_id:
            initial['selected_room_type'] = room_id
        return initial

class BookingSuccessView(TemplateView):
    template_name = "pages/booking_success.html"

class AboutView(TemplateView):
    template_name = "pages/about.html"

class ContactView(TemplateView):
    template_name = "pages/contact.html"
