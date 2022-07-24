import json

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DeleteView, CreateView, ListView, DetailView
from product.models import Product
from django.core.paginator import Paginator
from product.forms import AddForm
from django.core.validators import ValidationError


# Create your views here.


class HomeView(ListView):
    paginate_by = 6
    model = Product
    template_name = 'home.html'
    ordering = '-date'
    # success_url = reverse_lazy('home_page')

    def delete(request, id):
        product = Product.objects.get(id=id)
        product.delete()

        return redirect('home_page')


    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     for i in qs:
    #         jojo = self.kwargs['type_product']
    #         return qs

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     jojo = json.loads(data['point_2'])
    #     return jojo



class CreateView(SuccessMessageMixin, CreateView):
    model = Product
    form_class = AddForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        error = ''
        if self.request.method == 'POST':
            new = form.save(commit=False)
            if form.is_valid():
                h = self.request.POST.getlist('point')
                new.point_2 = h
                new.point = None
                # print(h)
                new.save()
            return super().form_valid(form)



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




