from django.db import models
from datetime import date
# Create your models here.

class Book(models.Model):
    book_id = models.IntegerField()
    book_name = models.CharField(max_length=30)
    book_price = models.IntegerField()
    subject = models.CharField(max_length=30)
    pub_date = models.DateField(default=date.today())
    
    def __str__(self):
        return self.book_name
