from django.db import models

class Emp(models.Model):
    empno = models.IntegerField()
    ename = models.CharField(max_length=30)
    sal = models.FloatField()
    job = models.CharField(max_length=20)
    deptno = models.IntegerField()
