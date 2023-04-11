# send mail
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save

from.models import Post


@receiver(post_save, sender=Post)
def notify_author(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject=f'{instance.title} created successfully',
            message=f'{instance.author}, your post created successfully. Date: {instance.post_time.strftime("%d %m %Y")}',
            from_email='kiryldorakh@yandex.ru',
            recipient_list=[f'{instance.author.email}']
        )
    else:
        send_mail(
            subject=f'{instance.title} changed successfully',
            message=f'{instance.author}, your post changed successfully. Date: {instance.post_time.strftime("%d %m %Y")}',
            from_email='kiryldorakh@yandex.ru',
            recipient_list=[f'{instance.author.email}']
        )