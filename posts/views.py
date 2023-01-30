from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Post

# WYSIWYG Editor
from .forms import PostCreateForm, PostUpdateForm

# D4 filters
from .filters import PostFilter


class PostListView(ListView):
    model = Post
    ordering = '-post_time'
    context_object_name = 'posts'
    template_name = 'posts/home.html'
    paginate_by = 5

    # D4 (filter)
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


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

