from django.db import models

from .category import Category


class Banner(models.Model):
    title = models.CharField(
        max_length=60,
        verbose_name="Название",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name="Категория",
    )

    price_from = models.PositiveIntegerField(
        verbose_name="Цена начинается с $",
    )

    photo = models.ImageField(
        upload_to='banners/',
        verbose_name='Баннер',
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
