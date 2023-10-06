from django.db import models

from user_profile.models import Users


# Create your models here.
class Orders(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Users, on_delete=models.PROTECT, related_name= "worker_name")
    client = models.ForeignKey(Users, on_delete=models.PROTECT, related_name= "client_name")
    price = models.FloatField()
    description = models.TextField()
    status = models.ForeignKey('Status', on_delete=models.PROTECT)

class Status (models.Model):
    name = models.CharField(max_length=255)