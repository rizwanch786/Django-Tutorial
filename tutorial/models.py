from django.db import models
from django.forms import EmailField
# Create your models here.

class Contact(models.Model):
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=300)
    
    def __str__(self):
        return str(self.email)