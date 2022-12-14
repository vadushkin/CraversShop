# Generated by Django 4.1.2 on 2022-10-11 14:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import phone_field.models
import shop.models.product


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='Слаг')),
                ('photo', models.FileField(blank=True, null=True, upload_to='categories/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['img', 'svg', 'png', 'jpeg', 'ico', 'webp', 'jpg'], message='Этот формат фотографии не подходит')], verbose_name='Фотография')),
                ('is_menu_field', models.BooleanField(verbose_name='Это категория меню?')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='shop.category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'unique_together': {('parent', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locate', models.CharField(max_length=150, verbose_name='Расположен')),
                ('phone', phone_field.models.PhoneField(help_text='Телефон', max_length=31)),
                ('email', models.EmailField(max_length=254, verbose_name='Емейл')),
            ],
            options={
                'verbose_name': 'Контактную запись',
                'verbose_name_plural': 'Контактные данные',
            },
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='logos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['img', 'svg', 'png', 'jpeg', 'ico', 'webp', 'jpg'], message='Этот формат фотографии не подходит')], verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Логотип',
                'verbose_name_plural': 'Логотипы',
            },
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('url', models.URLField(max_length=150, verbose_name='Ссылка')),
                ('photo', models.ImageField(upload_to='social_networks/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Социальная сеть',
                'verbose_name_plural': 'Социальные сети',
            },
        ),
        migrations.CreateModel(
            name='OurCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('url', models.URLField(max_length=100, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компания',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='Слаг')),
                ('description', models.TextField(max_length=300, verbose_name='Описание')),
                ('photo', models.FileField(upload_to='products/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['img', 'svg', 'png', 'jpeg', 'ico', 'webp', 'jpg'], message='Этот формат фотографии не подходит')], verbose_name='Фотография')),
                ('photo_back', models.FileField(blank=True, null=True, upload_to='products/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['img', 'svg', 'png', 'jpeg', 'ico', 'webp', 'jpg'], message='Этот формат фотографии не подходит')], verbose_name='Обратная фотография')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('sale', models.PositiveIntegerField(blank=True, default=0, validators=[shop.models.product.validate_even], verbose_name='Скидка')),
                ('stars', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default=1, max_length=1, verbose_name='Звёзды')),
                ('is_on_closeout', models.BooleanField(verbose_name='На распродаже?')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название')),
                ('description', models.CharField(max_length=60, verbose_name='Описание')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('photo', models.ImageField(upload_to='our_services/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Сервис',
                'verbose_name_plural': 'Сервисы',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('photo', models.ImageField(upload_to='our_services/', verbose_name='Фотография')),
                ('description', models.CharField(max_length=150, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Свидетельство',
                'verbose_name_plural': 'Свидетельство',
            },
        ),
        migrations.CreateModel(
            name='ProductOfTheDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество товаров')),
                ('sold', models.PositiveIntegerField(blank=True, null=True, verbose_name='Продано')),
                ('open', models.BooleanField(verbose_name='Открыта?')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Продукт дня',
                'verbose_name_plural': 'Продукты дня',
            },
        ),
        migrations.CreateModel(
            name='PopularCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Популярная Категория',
                'verbose_name_plural': 'Популярные Категории',
            },
        ),
        migrations.CreateModel(
            name='LowerBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название')),
                ('sale', models.PositiveIntegerField(blank=True, default=0, validators=[shop.models.product.validate_even], verbose_name='Скидка')),
                ('price_from', models.PositiveIntegerField(verbose_name='Цена начинается с $')),
                ('photo', models.ImageField(upload_to='lower_banner/', verbose_name='Баннер')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Нижний Баннер',
                'verbose_name_plural': 'Нижний Баннер',
            },
        ),
        migrations.CreateModel(
            name='BrandDirectoryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product', models.ManyToManyField(related_name='brand_products', to='shop.category')),
            ],
            options={
                'verbose_name': 'Категория Бренда',
                'verbose_name_plural': 'Категории Брендов',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='Слаг')),
                ('text', models.TextField(verbose_name='Текст')),
                ('photo', models.ImageField(upload_to='our_services/', verbose_name='Фотография')),
                ('stars', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default=1, max_length=1, verbose_name='Звёзды')),
                ('likes', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
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
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название')),
                ('price_from', models.PositiveIntegerField(verbose_name='Цена начинается с $')),
                ('photo', models.ImageField(upload_to='banners/', verbose_name='Баннер')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннеры',
            },
        ),
    ]
