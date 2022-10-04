from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse

from .category import Category


def validate_even(value):
    if not 0 <= int(value) < 100:
        raise ValidationError(f'{value} - должно быть от 1 до 99',
                              params={'value': value},
                              )


class Product(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название',
    )
    slug = models.SlugField(
        verbose_name="Слаг",
    )
    description = models.TextField(
        verbose_name="Описание",
        max_length=300,
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
    )
    photo = models.FileField(
        upload_to='products/',
        verbose_name='Фотография',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['img', 'svg', 'png', 'jpeg', 'ico', 'webp', 'jpg'],
                message="Этот формат фотографии не подходит"
            )],
    )
    photo_back = models.FileField(
        upload_to='products/',
        verbose_name='Обратная фотография',
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['img', 'svg', 'png', 'jpeg', 'ico', 'webp', 'jpg'],
                message="Этот формат фотографии не подходит"
            )],
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена",
        default=0,
    )
    sale = models.PositiveIntegerField(
        verbose_name="Скидка",
        default=0,
        blank=True,
        validators=[validate_even]
    )
    stars = models.CharField(
        max_length=1,
        choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)],
        default=1,
        verbose_name="Звёзды",
    )
    is_on_closeout = models.BooleanField(
        verbose_name="На распродаже?"
    )

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('product', args=[str(self.slug)])

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
