from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, Notification


@receiver(post_save, sender=Message)
def message_post_save(sender, instance, created, **kwargs):
    if created:
        # Logic to handle the creation of a new message
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )
        print(
            f"New message created: {instance.content} from {instance.sender} to {instance.receiver}")
