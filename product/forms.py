from django import forms
from product.models import Product
from django.forms import TextInput, DateTimeInput, FileInput, JSONField, DateInput, Textarea
from django.core.validators import ValidationError


class AddForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('type_product', 'date_delivery', 'image', 'point', 'point_2')
        a = 'dfsdf'
        widgets = {
            'type_product': TextInput(attrs={
                'label': 'dfasdf',
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

        labels = {
            'type_product': 'Тип товара',
        }


            # 'point': TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Адреса доставки'
            # })}


        # type_product = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={
        #     'class': 'form-control',
        #     'placeholder': 'Тип товара'
        # }))
        # date_delivery = forms.DateField(label="", widget=forms.DateInput(attrs={
        #     'class': 'form-control',
        #     'placeholder': 'Дата доставки'
        # }))
        # image = forms.ImageField(label="", widget=forms.FileInput(attrs={
        #     'class': 'form-control',
        #     'placeholder': 'Изображение продукта'
        # }))
        # point = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={
        #     'class': 'form-control',
        #     'placeholder': 'Адреса доставки'
        # }))