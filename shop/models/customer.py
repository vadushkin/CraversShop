from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    name = models.CharField(
        max_length=200,
        null=True,
        verbose_name="Имя"
    )
    email = models.EmailField(
        max_length=200,
        verbose_name="Емейл"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
