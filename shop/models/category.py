from django.core.validators import FileExtensionValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    slug = models.SlugField(verbose_name="Слаг")
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Родитель"
    )
    photo = models.FileField(upload_to='categories/', validators=[
        FileExtensionValidator(
            allowed_extensions=['img', 'svg', 'png', 'jpeg', 'ico', 'webp', 'jpg'],
            message="Этот формат фотографии не подходит"
        )], verbose_name='Фотография')

    def __str__(self):
        return f'{self.name} | Родитель - {self.parent}' if self.parent else self.name

    @classmethod
    def get_default_pk(cls):
        obj, created = cls.objects.get_or_create(name="No category")
        return obj.pk

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
