from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
import uuid

from account_transfare_app.models import Accounts, Transactions


class ViewsTest(TestCase):

    def setUp(self):
        self.account_uuid = uuid.uuid4()
        self.account = Accounts.objects.create(id=self.account_uuid, name='Test Account', balance=1000.00)

    def test_list_accounts_view(self):
        response = self.client.get(reverse('list_accounts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_accounts.html')

    def test_import_accounts_view(self):
        file = SimpleUploadedFile("test_file.csv", b"file_content", content_type="text/csv")
        response = self.client.post(reverse('import_accounts'), {'file': file})
        self.assertEqual(response.status_code, 302)

    def test_transfer_funds_view(self):
        response = self.client.get(reverse('transfer_funds'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'transfer_funds.html')

    def test_transfer_view(self):
        response = self.client.post(reverse('transfer'),
                                    {'sender_id': self.account_uuid, 'receiver_id': uuid.uuid4(), 'amount': 100.00})
        self.assertEqual(response.status_code, 302)

    def test_show_history_view(self):
        Transactions.objects.create(sender_id=self.account_uuid, receiver_id=self.account_uuid,
                                    sender_balance_before_transaction=1000.00,
                                    receiver_balance_before_transaction=1000.00, amount=100.00)
        response = self.client.get(reverse('show_history', args=[self.account_uuid]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'show_history.html')
