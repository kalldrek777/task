from django.contrib import admin
from product.models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    exclude = ['point']


admin.site.register(Product, ProductAdmin)