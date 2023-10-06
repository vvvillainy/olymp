from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    job = models.BooleanField()
    balance = models.FloatField(default=0)


class Money(models.Model):
    user = models.ForeignKey(Users, on_delete=models.PROTECT)
    where = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    sum = models.IntegerField()
