import uuid

from django.db import models


# Create your models here.


class Accounts(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=100, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Transactions(models.Model):
    sender = models.ForeignKey(Accounts, related_name='sent_transactions', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Accounts, related_name='received_transactions', on_delete=models.CASCADE)
    sender_balance_before_transaction = models.DecimalField(max_digits=100, decimal_places=3)
    receiver_balance_before_transaction = models.DecimalField(max_digits=100, decimal_places=3)
    amount = models.DecimalField(max_digits=100, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
