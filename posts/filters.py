from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'post_time': ['gt'],
            'headline': ['icontains'],
            'author': ['exact'],
        }

class CategoryFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'categories'
        }