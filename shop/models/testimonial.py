from django.db import models


class Testimonial(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Имя",
    )

    position = models.CharField(
        max_length=100,
        verbose_name="Должность",
    )

    photo = models.ImageField(
        upload_to='our_services/',
        verbose_name='Фотография',
    )

    description = models.CharField(
        max_length=150,
        verbose_name="Текст",
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Свидетельство'
        verbose_name_plural = 'Свидетельство'
