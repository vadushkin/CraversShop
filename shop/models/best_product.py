from django.db import models

from .product import Product


class BestProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name="Продукт",
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    def __str__(self):
        return f'{self.product}'

    class Meta:
        verbose_name = 'Лучший продукт'
        verbose_name_plural = 'Лучшие продукты'
