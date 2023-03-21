from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post, Category


class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Categories',
        conjoined=True,
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


# class CategoryFilter(FilterSet):
#     class Meta:
#         model = Post
#         fields = {
#             'category'
#         }


class UserPostsFilter(FilterSet):
    class Meta:
        model = Post
        fields = ['author']

    @property
    def qs(self):
        parent = super().qs
        author = getattr(self.request, 'user', None)

        return parent.filter(author=author)
