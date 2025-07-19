from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Todo

@receiver(post_save, sender=Todo)
def send_notification_on_create_or_update(sender, instance, created, **kwargs):
    if created:
        print(f"New Todo Created: {instance.task}")
        #or send email notification
    else:
        print(f"Todo Updated: {instance.task}")
        #or send email notification


@receiver(post_delete, sender=Todo)
def send_notification_on_delete(sender, instance, **kwargs):
    print(f"Todo Deleted: {instance.task}")
    #or send email notification