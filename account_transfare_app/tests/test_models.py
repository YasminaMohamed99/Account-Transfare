import uuid
from django.test import TestCase
from account_transfare_app.models import Accounts, Transactions


class ModelTest(TestCase):
    def setUp(self):
        self.sender = Accounts.objects.create(id=uuid.uuid4(), name='Sender Account', balance=1000.123)
        self.receiver = Accounts.objects.create(id=uuid.uuid4(), name='Receiver Account', balance=500.123)
        self.transaction = Transactions.objects.create(sender=self.sender, receiver=self.receiver, sender_balance_before_transaction=self.sender.balance, receiver_balance_before_transaction=self.receiver.balance, amount=100.123)

    def test_account_creation(self):
        self.assertIsInstance(self.sender, Accounts)
        self.assertEqual(self.sender.name, 'Sender Account')
        self.assertEqual(self.sender.balance, 1000.123)

    def test_account_str(self):
        self.assertEqual(str(self.sender), 'Sender Account')

    def test_transaction_creation(self):
        self.assertIsInstance(self.transaction, Transactions)
        self.assertEqual(self.transaction.sender, self.sender)
        self.assertEqual(self.transaction.receiver, self.receiver)
        self.assertEqual(self.transaction.sender_balance_before_transaction, 1000.123)
        self.assertEqual(self.transaction.receiver_balance_before_transaction, 500.123)
        self.assertEqual(self.transaction.amount, 100.123)