from django.db import models


class Users(models.Model):
    login = models.CharField('login', max_length=50)
    password = models.CharField('password', max_length=50)
    role = models.CharField('role', max_length=50)


class ParkingList(models.Model):
    Number = models.CharField('Number', max_length=2)
    Status = models.CharField('Status', max_length=40)
    TimeStart = models.CharField('TimeStart', max_length=40, default= '00:00')
    TimeEnd = models.CharField('TimeEnd', max_length=40, default= '00:00')
