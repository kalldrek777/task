# Generated by Django 4.0.6 on 2022-07-22 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='point',
            field=models.JSONField(max_length=50, verbose_name='адреса доставки'),
        ),
    ]