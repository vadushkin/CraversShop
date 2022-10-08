# Generated by Django 4.1.1 on 2022-10-06 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_productoftheday_options_productoftheday_open_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Лучший продукт',
                'verbose_name_plural': 'Лучшие продукты',
            },
        ),
    ]