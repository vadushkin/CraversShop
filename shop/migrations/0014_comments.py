# Generated by Django 4.1.1 on 2022-10-07 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0013_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.blog', verbose_name='Блок')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментария',
            },
        ),
    ]
