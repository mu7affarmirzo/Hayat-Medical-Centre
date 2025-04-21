from django.db import models


class NotificationModel(models.Model):
    sender = models.ForeignKey('Account', related_name='sent_notifications', on_delete=models.SET_NULL, null=True, blank=True)
    receiver = models.ForeignKey('Account', related_name='notifications', on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    state = models.BooleanField(default=False)

    generated_url = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.receiver} | {self.message[:50]}'
