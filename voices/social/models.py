from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    heading = models.CharField(max_length=128)
    description = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
