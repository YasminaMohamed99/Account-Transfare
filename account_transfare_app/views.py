from django.shortcuts import render
from django.http import HttpResponse

from account_transfare_app.models import Accounts


def list_accounts(request):
    # account1 = Accounts.objects.create(id="cc26b56c-36f6-41f1-b689-d1d5065b95af", name="Joy Dean", balance=4497.22)
    # account2 = Accounts.objects.create(id="be6acfdc-cae1-4611-b3b2-dfb5167ba5fe", name="Bryan Rice", balance=2632.76)
    # account1.save()
    # account2.save()
    return HttpResponse("Hello, world. You're at the myapp index.")
