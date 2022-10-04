from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    title = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название',
    )
    slug = models.SlugField(
        verbose_name="Слаг",
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        db_index=True,
        related_name='children',
        verbose_name='Родительская категория',
    )
    photo = models.FileField(
        upload_to='categories/',
        blank=True,
        null=True,
        verbose_name='Фотография',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['img', 'svg', 'png', 'jpeg', 'ico', 'webp', 'jpg'],
                message="Этот формат фотографии не подходит"
            )],
    )
    is_menu_field = models.BooleanField(verbose_name="Это категория меню?")

    def __str__(self):
        return f'{self.title} | Родитель - {self.parent}' if self.parent else self.title

    @classmethod
    def get_default_pk(cls):
        obj, created = cls.objects.get_or_create(name="No category")
        return obj.pk

    def get_absolute_url(self):
        return reverse('posts-by-category', args=[str(self.slug)])

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
