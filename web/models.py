from django.db import models
#from __future__ import unicode_literals
from django.contrib.auth.models import User
# Create your models here.
class expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    def __str__ (self):
        return self.text
class income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.PROTECT)
