# Generated by Django 4.0.6 on 2022-07-22 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='point',
            field=models.JSONField(default={}, max_length=50, verbose_name='адреса доставки'),
        ),
    ]
