from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        author_id = str(self.user.username)
        return author_id


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)

    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def preview(self):
        return self.body[:120] + "..."

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с постом
    # def get_absolute_url(self):
    #     return f'/news/{self.id}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    comment_text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text




