from django.urls import path
from .views import DishReviewCreateView

urlpatterns = [
    path('dish/<int:dish_id>/review/', DishReviewCreateView.as_view(), name='dish_review_add'),
]