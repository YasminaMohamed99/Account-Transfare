from django.db import models


# Create your models here.


class Accounts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=10)


class Transactions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sender_id = models.CharField(max_length=255)
    receiver_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=10)
