from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class MenuCategory(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField()
    photo = models.FileField(upload_to='categories/', blank=True, null=True, validators=[
        FileExtensionValidator(
            allowed_extensions=['img', 'svg', 'png', 'jpeg', 'ico', 'webp', 'jpg'],
            message="Этот формат фотографии не подходит"
        )], verbose_name='Фотография')

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория меню'
        verbose_name_plural = 'Категории меню'

    def get_absolute_url(self):
        return reverse('posts-by-category', args=[str(self.slug)])

    def __str__(self):
        return f'{self.title} | Родитель - {self.parent}' if self.parent else self.title
