from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Post, Comment

# WYSIWYG Editor
from .forms import PostCreateForm, PostUpdateForm, CommentCreateForm, CommentResponseForm

# D4 filters
from .filters import PostFilter, CommentFilter

# D5 Authorization
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# permissions
from django.views import View
from django.shortcuts import redirect

# Comment
from django.shortcuts import get_object_or_404

# send mail
from django.core.mail import send_mail


# List Views
class PostListView(ListView):
    model = Post
    ordering = '-post_time'
    context_object_name = 'posts'
    template_name = 'posts/home.html'
    paginate_by = 6


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    ordering = '-post_time'
    context_object_name = 'posts'
    template_name = 'posts/user_posts.html'
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(author=self.request.user)
        return qs


class PostSearchList(LoginRequiredMixin, ListView):
    model = Post
    ordering = '-post_time'
    context_object_name = 'posts'
    template_name = 'posts/search.html'
    paginate_by = 6

    # D4 (filter)
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class CommentsPostListView(LoginRequiredMixin, ListView):
    model = Post
    ordering = '-post_time'
    context_object_name = 'posts'
    template_name = 'posts/comments.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(author=self.request.user)
        self.filterset = CommentFilter(self.request.GET,  request=self.request, queryset=qs)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


# Comment Views
class CommentResponse(UpdateView):
    model = Comment
    template_name = 'posts/comment_response.html'
    form_class = CommentResponseForm
    success_url = reverse_lazy('comments')

    def post(self, request, *args, **kwargs):
        next_url = self.request.GET.get('next', None)
        comment = Comment.objects.get(pk=kwargs['pk'])
        form = CommentResponseForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            # send mail
            send_mail(
                subject=f'{comment.post.author} sent accept a response to the task {comment.post.title}',
                message=f'{comment.user} your response is accepted by {comment.post.author}',
                from_email='kiryldorakh@yandex.ru',
                recipient_list=[f'{comment.user.email}']
            )
            if next_url:
                return redirect(next_url)
            else:
                return super().form_valid(form)
        else:
            return render(request, 'posts/comment_response.html', {'form': form, 'comment': comment})


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'posts/comment.html'
    form_class = CommentCreateForm

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'posts/comment_delete.html'
    context_object_name = 'comment'

    def get_success_url(self):
        next_url = self.request.GET.get('next', None)
        if next_url:
            return next_url
        else:
            return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})


# Post Views
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.get_object()
            comment.save()

            # send mail
            send_mail(
                subject=f'{comment.user} sent a response to the task {comment.post.title}',
                message=f'{comment.comment_text}',
                from_email='kiryldorakh@yandex.ru',
                recipient_list=[f'{comment.post.author.email}']
            )

            return redirect(request.path_info)
        else:
            return render(request, self.template_name, {'post': self.get_object(), 'comment_form': form})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/post_new.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('user_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user

        # send_mail(
        #     subject=f'{form.instance.title} created successfully',
        #     message=f'{form.instance.author}, your post created successfully',
        #     from_email='kiryldorakh@yandex.ru',
        #     recipient_list=[f'{form.instance.author.email}']
        # )

        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'posts/post_edit.html'
    form_class = PostUpdateForm
    # fields = ['title', 'body', 'category']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('user_posts')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# not working
class CustomPermissionDeniedView(View):
    template_name = 'posts/permission_denied.html'

    def get(self, request):
        return render(request, self.template_name)


