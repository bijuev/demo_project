from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    name = models.CharField(max_length=120, default="John Doe")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.name

