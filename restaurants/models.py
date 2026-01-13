from django.db import models
from django.conf import settings
from core.models import TimeStampedModel

class Restaurant(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name="Название ресторана")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    contact_info = models.TextField(verbose_name="Контактная информация")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    logo = models.ImageField(upload_to='logos/', blank=True, null=True, verbose_name="Логотип")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"