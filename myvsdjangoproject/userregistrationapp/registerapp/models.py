from django.db import models
class UserModel(models.Model):
    userid = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=30)
    def __str__(self):
        return self.userid+","+self.password+","+self.username
