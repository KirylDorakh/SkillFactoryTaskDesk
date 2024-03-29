from django import forms
from .models import Post, Comment

# WYSIWYG Editor
from django_summernote.widgets import SummernoteWidget
# from django_summernote.fields import SummernoteTextFormField

# D4 forms
from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model


class PostCreateForm(forms.ModelForm):
    body = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ['title', 'body', 'category']


class PostUpdateForm(forms.ModelForm):
    body = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ['title', 'body', 'category']


class CommentCreateForm(forms.ModelForm):
    comment_text = forms.CharField(label='Leave your response here',
                                   widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ['comment_text']


class CommentResponseForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['is_responded']


# D4 Forms
class PostForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'body',
            'category',
        ]

    # проверка данных в форме
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return name


