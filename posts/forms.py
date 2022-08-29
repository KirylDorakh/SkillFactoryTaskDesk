from django import forms
from .models import Post

# WYSIWYG Editor
from django_summernote.widgets import SummernoteWidget


class PostCreateForm(forms.ModelForm):
    body = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ['title', 'author', 'body', 'category']


class PostUpdateForm(forms.ModelForm):
    body = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ['title', 'body', 'category']

