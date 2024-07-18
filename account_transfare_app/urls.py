from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_accounts, name='list_accounts'),
    path('import_accounts', views.import_accounts, name='import_accounts'),
    path('transfer_funds', views.transfer_funds, name='transfer_funds'),
]