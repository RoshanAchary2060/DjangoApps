from django.db import models

class RegisterModel(models.Model):
    userid = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
