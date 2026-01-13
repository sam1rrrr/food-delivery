from django.urls import path
from .views import (
    RestaurantListView, 
    RestaurantCreateView, 
    RestaurantUpdateView, 
    RestaurantDeleteView,
    RestaurantDetailView
)

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurant_list'),
    path('add/', RestaurantCreateView.as_view(), name='restaurant_add'),
    path('<int:pk>/edit/', RestaurantUpdateView.as_view(), name='restaurant_edit'),
    path('<int:pk>/delete/', RestaurantDeleteView.as_view(), name='restaurant_delete'),
    path('<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
]