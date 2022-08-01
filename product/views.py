from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from product.models import Product
from django.core.paginator import Paginator
from product.forms import AddForm, DayForm, FormSet
from django.core.validators import ValidationError
from product.utils import *


class HomeView(DataMixin, ListView):
    paginate_by = 6
    model = Product
    template_name = 'home.html'
    ordering = '-date'

    def delete(request, id):
        product = Product.objects.get(id=id)
        product.delete()

        return redirect('home_page')


class CreateView(DataMixin, CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = AddForm
    success_url = reverse_lazy('home_page')

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['special_form'] = FormSet()
        return ctx

    def form_valid(self, form):
        special_form = FormSet(self.request.POST, self.request.FILES)
        form2 = AddForm(self.request.POST, self.request.FILES)
        if special_form.is_valid() and form2.is_valid():
            new = form2.save(commit=False)
            for f in special_form:
                if f.cleaned_data.get('point') != None:
                    tt = self.request.POST.getlist('form-0-point')
                    new.point_2 = tt
                    new.save()
            return redirect('home_page')
        else:
            print('d')
            return redirect("add_page")








# def home(request):
#     qs = Product.objects.all().order_by('-date')
#     paginator = Paginator(qs, 6)  # Show 8 contacts per page.
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     dict = {'page_obj': page_obj}
#
#     return render(request, 'home.html', dict)
#
#
# def add_product(request):
#     error = ''
#     form = AddForm()
#     if request.method == 'POST':
#         form = AddForm(request.POST, request.FILES)
#         new_user = form.save(commit=False)
#         if form.is_valid():
#             h = request.POST.getlist('point')
#             new_user.point_2 = h
#             print(h)
#             new_user.save()
#             return redirect('home_page')
#         else:
#             error = 'Форма была неверной'
#
#     return render(request, 'add_product.html', {'form': form, 'error': error})




