from django.db import models
from users.models import User
from django.utils import timezone


class Income(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="income", null=True, blank=True)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.description} - {self.amount} on {self.date}'
