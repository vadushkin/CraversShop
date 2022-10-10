from django.core.validators import FileExtensionValidator
from django.db import models


class Logo(models.Model):
    photo = models.FileField(
        upload_to='logos/',
        verbose_name='Логотип',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['img', 'svg', 'png', 'jpeg', 'ico', 'webp', 'jpg'],
                message="Этот формат фотографии не подходит"
            )],
    )

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = "Логотип"
        verbose_name_plural = "Логотипы"
