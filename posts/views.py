from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Post

# WYSIWYG Editor
from .forms import PostCreateForm, PostUpdateForm


class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    content_object_name = 'all_posts_list'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    form_class = PostCreateForm
    # fields = ['title', 'body', 'category', 'author']


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    form_class = PostUpdateForm
    # fields = ['title', 'body', 'category']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

