from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Restaurant
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

from core.mixins import OwnerRequiredMixin
class RestaurantPaginationMixin:
    paginate_by = 3 

class RestaurantListView(RestaurantPaginationMixin, ListView):
    model = Restaurant
    template_name = 'restaurants/list.html'
    context_object_name = 'restaurants'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Restaurant.objects.filter(
                Q(name__icontains=query) | 
                Q(description__icontains=query) |
                Q(dishes__name__icontains=query)
            ).distinct()
        return Restaurant.objects.all()

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    model = Restaurant
    fields = ['name', 'address', 'contact_info', 'description', 'logo']
    template_name = 'restaurants/create.html'
    success_url = '/restaurants/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class RestaurantUpdateView(OwnerRequiredMixin, UpdateView):
    model = Restaurant
    fields = ['name', 'address', 'contact_info', 'description', 'logo']
    template_name = 'restaurants/create.html'
    success_url = '/restaurants/'

class RestaurantDeleteView(OwnerRequiredMixin, DeleteView):
    model = Restaurant
    template_name = 'restaurants/delete.html'
    success_url = reverse_lazy('restaurant_list')


class RestaurantDetailView(OwnerRequiredMixin, DetailView):
    model = Restaurant
    template_name = 'restaurants/detail.html'
    context_object_name = 'restaurant'