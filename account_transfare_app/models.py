import uuid

from django.db import models


# Create your models here.


class Accounts(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=100, decimal_places=10)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Transactions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sender_id = models.CharField(max_length=255)
    receiver_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=100, decimal_places=10)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
