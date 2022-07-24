# Generated by Django 4.0.6 on 2022-07-21 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_product_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата создания товара'),
            preserve_default=False,
        ),
    ]