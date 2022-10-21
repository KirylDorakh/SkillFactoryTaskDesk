from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Post

# WYSIWYG Editor
from .forms import PostCreateForm, PostUpdateForm


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/home.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_new.html'
    form_class = PostCreateForm
    # fields = ['title', 'body', 'category', 'author']


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_edit.html'
    form_class = PostUpdateForm
    # fields = ['title', 'body', 'category']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('home')

