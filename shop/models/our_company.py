from django.db import models


class OurCompany(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    url = models.URLField(max_length=100, verbose_name="Ссылка")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компания"
