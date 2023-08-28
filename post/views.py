from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Post


class PostList(ListView):
    model = Post

    template_name = "post/list.html"


class PostCreate(CreateView):
    model = Post

    template_name = "post/create.html"

    fields = "__all__"

    success_url = "/post"


class PostUpdate(UpdateView):
    model = Post

    template_name = "post/update.html"

    fields = "__all__"

    success_url = "/post"


class PostDelete(DeleteView):
    model = Post

    success_url = "/post"
