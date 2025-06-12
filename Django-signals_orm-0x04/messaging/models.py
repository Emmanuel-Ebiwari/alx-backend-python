from django.db import models

# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp}"


class Notification(models.Model):
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='notifications')
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name='notifications')
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user} regarding message {self.message.id} at {self.timestamp}"
