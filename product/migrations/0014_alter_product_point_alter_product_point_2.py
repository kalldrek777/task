# Generated by Django 4.0.6 on 2022-07-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_product_point_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='point',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='адреса доставки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='point_2',
            field=models.JSONField(blank=True, null=True, verbose_name='адреса доставки'),
        ),
    ]
