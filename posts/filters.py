from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter
from django.forms import DateTimeInput, SelectMultiple
from .models import Post, Category


def my_posts(request):
    if request is None:
        return Post.objects.none()
    user = request.user
    return Post.objects.filter(author=user)


class CommentFilter(FilterSet):
    title = ModelMultipleChoiceFilter(
        field_name='title',
        queryset=my_posts,
        label='Task title',
        widget=SelectMultiple(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Post
        fields = ['title']


class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Categories',
        conjoined=True,
        widget=SelectMultiple(attrs={'class': 'form-control'}),
    )

    post_time = DateTimeFilter(
        field_name='post_time',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['exact'],
        }
