from django.contrib import admin

from account_transfare_app.models import Accounts, Transactions

# Register your models here.

admin.site.register(Accounts)


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('sender_id', 'receiver_id', 'sender_balance_before_transaction', 'receiver_balance_before_transaction', 'amount', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('sender_id', 'receiver_id')
