# Generated by Django 4.0.6 on 2022-07-21 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_point_product_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
    ]
