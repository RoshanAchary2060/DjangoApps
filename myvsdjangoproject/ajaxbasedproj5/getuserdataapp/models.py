from django.db import models

# Create your models here.

class Emp(models.Model):
    empno = models.IntegerField()
    ename = models.CharField(max_length=30)
    sal = models.IntegerField()
    job = models.CharField(max_length=30)
