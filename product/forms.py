from django import forms
from product.models import Product
from django.forms import TextInput, DateTimeInput, FileInput, JSONField, DateInput, Textarea, modelformset_factory, \
    ModelForm, formset_factory
import datetime
from django.core.validators import ValidationError


class DayForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('point',)
        widgets = {
            'point': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адреса доставки',
            })
        }


class AddForm(ModelForm):

    class Meta:
        model = Product
        fields = ('type_product', 'date_delivery', 'image', 'point_2')
        a = 'dfsdf'
        widgets = {
            'type_product': TextInput(attrs={
                'max-length': '29',
                'class': 'form-control',
                'placeholder': 'Тип товара',
            }),
            'date_delivery': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата доставки',
                'input_formats': ['%d-%m-%Y'],
                'type': 'date'

            }),
            'image': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Изображение'
            }),
            'point': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адреса доставки',
            }),
            'point_2': TextInput(attrs={
                'type': 'hidden',
                'class': 'form-control',
                'placeholder': 'Адреса доставки',
            })}


# FormSet = modelformset_factory(Product, fields=('point',))

FormSet = formset_factory(DayForm, extra=1,)