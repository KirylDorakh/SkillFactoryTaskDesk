# Generated by Django 4.0.5 on 2023-04-10 17:02

from django.db import migrations, models


def set_default_false(apps, schema_editor):
    Post = apps.get_model('posts', 'Post')
    Post.objects.all().update(published=False)


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_responded',
            field=models.BooleanField(default=False),
        ),
    ]
