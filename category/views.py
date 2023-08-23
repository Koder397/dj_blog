from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Category


class CategoryList(ListView):
    model = Category

    template_name = 'category/list.html'


class CategoryCreate(CreateView):
    model = Category

    template_name = 'category/create.html'

    fields = '__all__'

    success_url = '/category'


class CategoryUpdate(UpdateView):
    model = Category

    template_name = 'category/update.html'

    fields = '__all__'

    success_url = '/category'


class CategoryDelete(DeleteView):
    model = Category

    success_url = '/category'
