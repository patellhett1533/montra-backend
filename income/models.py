from django.db import models
from users.models import User


class Income(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="income")
    amount = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.description} - {self.amount}'
