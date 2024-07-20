# tests/test_urls.py
from django.test import TestCase
from django.urls import reverse, resolve
from account_transfare_app import views
import uuid

from account_transfare_app.models import Accounts


class UrlTest(TestCase):

    def test_list_accounts_url(self):
        url = reverse('list_accounts')
        self.assertEqual(resolve(url).func, views.list_accounts)

    def test_import_accounts_url(self):
        url = reverse('import_accounts')
        self.assertEqual(resolve(url).func, views.import_accounts)

    def test_transfer_funds_url(self):
        url = reverse('transfer_funds')
        self.assertEqual(resolve(url).func, views.transfer_funds)

    def test_transfer_url(self):
        url = reverse('transfer')
        self.assertEqual(resolve(url).func, views.transfer)

    def test_show_history_url(self):
        test_uuid = uuid.uuid4()
        url = reverse('show_history', args=[test_uuid])
        self.assertEqual(resolve(url).func, views.show_history)

class UrlsResponseTest(TestCase):
    def setUp(self):
        self.account_uuid = uuid.uuid4()
        self.account = Accounts.objects.create(id=self.account_uuid, name='Test Account', balance=1000.00)
    def test_list_accounts_url(self):
        response = self.client.get(reverse('list_accounts'))
        self.assertEqual(response.status_code, 200)

    def test_import_accounts_url(self):
        response = self.client.get(reverse('import_accounts'))
        self.assertEqual(response.status_code, 200)

    def test_transfer_funds_url(self):
        response = self.client.get(reverse('transfer_funds'))
        self.assertEqual(response.status_code, 200)

    def test_transfer_url(self):
        response = self.client.get(reverse('transfer'))
        self.assertEqual(response.status_code, 200)

    def test_show_history_url(self):
        response = self.client.get(reverse('show_history', args=[self.account_uuid]))
        self.assertEqual(response.status_code, 200)
