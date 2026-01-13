from django.db import models
from django.contrib.auth.models import User
from menus.models import Dish
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.contrib.auth.models import User

from core.models import TimeStampedModel


class Review(TimeStampedModel):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField()

    def __str__(self):
        return f"Отзыв от {self.user.username}"