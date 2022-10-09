# Generated by Django 4.1.2 on 2022-10-09 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LowerBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название')),
                ('price_from', models.PositiveIntegerField(verbose_name='Цена начинается с $')),
                ('photo', models.ImageField(upload_to='lower_banner/', verbose_name='Баннер')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Нижний Баннер',
                'verbose_name_plural': 'Нижний Баннер',
            },
        ),
    ]
