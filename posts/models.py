from django.db import models

from django.contrib.auth.models import User


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        author_id = str(self.user.username)
        return author_id


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)

    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    comment_text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)



