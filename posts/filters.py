from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'post_time': ['gt'],
            'title': ['icontains'],
            'author': ['exact'],
            'category': ['exact'],
        }


# class CategoryFilter(FilterSet):
#     class Meta:
#         model = Post
#         fields = {
#             'category'
#         }
