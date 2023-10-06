from django.db import models

from user_profile.models import Users


# Create your models here.
class Orders(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Users, on_delete=models.PROTECT, related_name="worker_name")
    client = models.ForeignKey(Users, on_delete=models.PROTECT, related_name="client_name")
    price = models.FloatField()
    description = models.TextField()
    status = models.ForeignKey('Status', on_delete=models.PROTECT)


class Status(models.Model):
    name = models.CharField(max_length=255)


'''
id и статусы
1) Опубликован
2)В работе
3)Отменён
4)На доработке
5)Выполнен
6)Удалён
7)На проверке
'''


class Commentaries(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.PROTECT)
    number = models.IntegerField()
    text = models.TextField()
    version = models.FileField(upload_to=".")