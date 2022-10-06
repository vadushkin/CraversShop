from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=60, verbose_name="Название")
    description = models.CharField(max_length=60, verbose_name="Описание")
    url = models.URLField(verbose_name="Ссылка")
    photo = models.ImageField(upload_to='our_services/', verbose_name='Фотография')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"
