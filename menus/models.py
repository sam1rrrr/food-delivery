from django.db import models
from core.models import TimeStampedModel

class Dish(TimeStampedModel):
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=255, verbose_name="Название блюда")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to='dish_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"