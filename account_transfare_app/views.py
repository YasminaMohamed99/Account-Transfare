from django.shortcuts import render
from django.http import HttpResponse


def list_accounts(request):
    return HttpResponse("Hello, world. You're at the myapp index.")
