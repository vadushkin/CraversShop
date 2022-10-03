# Generated by Django 4.1.1 on 2022-10-03 15:31

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_category_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.category', verbose_name='Родитель'),
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('slug', models.SlugField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='children', to='shop.menucategory', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория меню',
                'verbose_name_plural': 'Категории меню',
                'unique_together': {('parent', 'slug')},
            },
        ),
    ]
