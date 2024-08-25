from django.db import models
from users.models import User


class Tranfer(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transfer")
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f'{self.amount} transfer to {self.name} on date {self.date}'
