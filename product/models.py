from django.db import models


# Create your models here.

class Product(models.Model):
    type_product = models.CharField(max_length=50, unique=False, verbose_name='тип товара', null=True, blank=True)
    date_delivery = models.DateField(unique=False, verbose_name='дата доставки', null=True, blank=True)
    image = models.ImageField(unique=False, verbose_name='изображение товара', null=True, blank=True)
    point = models.CharField(max_length=50, verbose_name='адреса доставки', null=True, blank=True)
    point_2 = models.JSONField(verbose_name='адреса доставки', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания товара')

    def __str__(self):
        return self.type_product

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['type_product']