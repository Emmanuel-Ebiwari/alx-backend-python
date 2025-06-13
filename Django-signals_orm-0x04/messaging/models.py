from django.db import models

# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    edited = models.BooleanField(default=False)
    parent_message = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')
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


class MessageHistory(models.Model):
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name='history')
    edited_by = models.ForeignKey(
        'auth.User', on_delete=models.SET_NULL, null=True, related_name='message_history')
    edited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-edited_at']

    def __str__(self):
        return f"History for message {self.message.id}: {self.action} at {self.edited_at}"
