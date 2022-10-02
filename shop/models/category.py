from django.core.validators import FileExtensionValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    slug = models.SlugField(verbose_name="Слаг")
    photo = models.FileField(upload_to='categories/', validators=[
        FileExtensionValidator(
            allowed_extensions=['img', 'svg', 'png', 'jpeg', 'ico', 'webp'],
            message="Этот формат фотографии не подходит"
        )], verbose_name='Фотография')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
