from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from .models import Dish
from restaurants.models import Restaurant
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from core.mixins import OwnerRequiredMixin

class DishCreateView(CreateView, LoginRequiredMixin):
    model = Dish
    fields = ['name', 'price', 'description', 'image']
    template_name = 'menus/dish_form.html'

    def form_valid(self, form):
        restaurant = get_object_or_404(Restaurant, pk=self.kwargs['restaurant_id'])
        form.instance.restaurant = restaurant
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('restaurant_detail', kwargs={'pk': self.kwargs['restaurant_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['restaurant_id'] = self.kwargs['restaurant_id']
        context['restaurant'] = get_object_or_404(Restaurant, pk=self.kwargs['restaurant_id'])
        return context


class DishDetailView(OwnerRequiredMixin, DetailView):
    model = Dish
    template_name = 'menus/dish_detail.html'
    context_object_name = 'dish'


class DishUpdateView(OwnerRequiredMixin, UpdateView):
    model = Dish
    fields = ['name', 'price', 'description', 'image']
    template_name = 'menus/dish_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['restaurant_id'] = self.object.restaurant.id
        return context

    def get_success_url(self):
        return reverse('dish_detail', kwargs={'pk': self.object.pk})

class DishDeleteView(OwnerRequiredMixin, DeleteView):
    model = Dish
    template_name = 'menus/dish_delete.html'

    def get_success_url(self):
        return reverse('restaurant_detail', kwargs={'pk': self.object.restaurant.pk})