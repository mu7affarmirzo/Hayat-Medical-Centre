from django.db import models

from apps.account.models import Account


class AttendanceModel(models.Model):
    staff = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='attendance')
    created_at = models.DateTimeField(auto_now_add=True)
    is_at_work = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f"{self.staff}-{self.is_at_work}"
