from django.db import models

class Books(models.Model):
    book_id = models.IntegerField()
    book_name = models.CharField(max_length=30)
    book_price = models.IntegerField()
    subject = models.CharField(max_length=30)

