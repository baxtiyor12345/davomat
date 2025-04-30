from django.db import models
from ..models import *


class Payme(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="payme")
    group=models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    amount=models.IntegerField()
    payme_date=models.DateTimeField(auto_now_add=True)
    method=models.CharField(max_length=50, choices=[
        ('cash','Cash'),
        ('card', 'Card'),
        ('online','Online')
    ])
    is_paid=models.BooleanField(default=True)
    note=models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.phone_number}-{self.amount} so`m"