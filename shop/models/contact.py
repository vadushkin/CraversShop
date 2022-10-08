from django.db import models
from phone_field import PhoneField


class Contact(models.Model):
    locate = models.CharField(max_length=150, verbose_name="Расположен")
    phone = PhoneField(help_text='Телефон')
    email = models.EmailField(verbose_name="Емейл")

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = "Контактную запись"
        verbose_name_plural = "Контактные данные"
