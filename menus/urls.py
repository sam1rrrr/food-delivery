from django.urls import path
from . import views

urlpatterns = [
    path('dish/add/<int:restaurant_id>/', views.DishCreateView.as_view(), name='dish_add'),
    path('dish/<int:pk>/edit/', views.DishUpdateView.as_view(), name='dish_edit'),
    path('dish/<int:pk>/delete/', views.DishDeleteView.as_view(), name='dish_delete'),
    path('dish/<int:pk>/', views.DishDetailView.as_view(), name='dish_detail')
]