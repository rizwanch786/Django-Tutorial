from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=300)

    def __str__(self):
        return str(self.email)


class ToDo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=1000)
    published_date = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)
