from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Review
from menus.models import Dish

class DishReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['rating', 'text']
    template_name = 'reviews/form.html'

    def form_valid(self, form):
        form.instance.dish = get_object_or_404(Dish, pk=self.kwargs['dish_id'])
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dish_detail', kwargs={'pk': self.kwargs['dish_id']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dish'] = get_object_or_404(Dish, pk=self.kwargs['dish_id'])
        return context