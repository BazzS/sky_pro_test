from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)
    specialty = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    education = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    portfolio = models.URLField()
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
