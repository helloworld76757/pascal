from django.db import models
# Create your models here.


class Event(models.Model):
    date = models.BigIntegerField()
    name = models.CharField(max_length=256)
    value = models.IntegerField()


class Alert(models.Model):
    timestamp = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    value = models.IntegerField()


class AlertResponse(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    alerts = models
