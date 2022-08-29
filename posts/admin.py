from django.contrib import admin

from .models import Post, Author, Category

# WYSIWYG Editor
from django_summernote.admin import SummernoteModelAdmin


# WYSIWYG Editor
class PostAdmin(SummernoteModelAdmin):
    # list_display = ('title', 'author', 'body', 'post_time', 'category')
    # list_filter = ("category",)
    # search_fields = ('title', 'content')
    # prepopulated_fields = {'category': ('title',)}
    summernote_fields = ('body',)


admin.site.register(Post, PostAdmin)

# admin.site.register(Post)
# admin.site.register(Author)
# admin.site.register(Category)
