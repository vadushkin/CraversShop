from django.db import models

from .category import Category
from .product import validate_even


class LowerBanner(models.Model):
    title = models.CharField(
        max_length=60,
        verbose_name="Название",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name="Категория",
    )

    sale = models.PositiveIntegerField(
        verbose_name="Скидка",
        default=0,
        blank=True,
        validators=[validate_even],
    )

    price_from = models.PositiveIntegerField(
        verbose_name="Цена начинается с $",
    )

    photo = models.ImageField(
        upload_to='lower_banner/',
        verbose_name='Баннер',
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Нижний Баннер"
        verbose_name_plural = "Нижний Баннер"
