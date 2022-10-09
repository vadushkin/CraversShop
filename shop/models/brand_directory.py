from django.db import models


from shop.models import Category


class BrandDirectoryCategory(models.Model):
    name = models.CharField(max_length=50)
    product = models.ManyToManyField(
        Category,
        related_name="brand_products"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория Бренда'
        verbose_name_plural = 'Категории Брендов'
