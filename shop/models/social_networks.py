from django.db import models


class Network(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    url = models.URLField(max_length=150, verbose_name="Ссылка")
    photo = models.ImageField(upload_to='social_networks/', verbose_name='Фотография')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"
