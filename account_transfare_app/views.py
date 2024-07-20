import uuid
from decimal import Decimal

import pandas as pd
from django.contrib import messages
from django.db import transaction, IntegrityError
from django.db.models import Q
from django.shortcuts import render, redirect
from account_transfare_app.forms import UploadFileForm
from account_transfare_app.models import Accounts, Transactions


def list_accounts(request):
    accounts = Accounts.objects.all()
    return render(request, "list_accounts.html", {"accounts": accounts})


def import_accounts(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_extension = file.name.split('.')[-1].lower()

            if file_extension == 'csv':
                df = pd.read_csv(file)
            elif file_extension == 'tsv':
                df = pd.read_csv(file, delimiter='\t')
            elif file_extension in ['xls', 'xlsx']:
                df = pd.read_excel(file)
            else:
                messages.error(request, "Unsupported file type, File types supported are (csv, tsv, xls, xlsx)")

            for _, row in df.iterrows():
                account_id = uuid.UUID(row['ID'])
                account, created = Accounts.objects.get_or_create(id=account_id, defaults={'name': row['Name'],
                                                                                           'balance': row['Balance']})
                if not created:
                    account.name = row['Name']
                    account.balance = row['Balance']
                    account.save()
            messages.success(request, "Accounts Imported Successfully!")
            return redirect('list_accounts')
    else:
        form = UploadFileForm()

    return render(request, 'list_accounts.html', {'form': form})


def transfer_funds(request):
    return render(request, "transfer_funds.html")


def transfer(request):
    if request.method == 'POST':
        sender_id = request.POST.get('sender-id')
        receiver_id = request.POST.get('receiver-id')
        amount = Decimal(request.POST.get('amount'))
        if not (sender_id and receiver_id and amount):
            messages.error(request, "All fields required!")
            return redirect('transfer_funds')
        try:
            with transaction.atomic():
                sender = Accounts.objects.select_for_update().get(id=sender_id) or None
                receiver = Accounts.objects.select_for_update().get(id=receiver_id) or None

                sender_balance = sender.balance
                receiver_balance = receiver.balance

                if not sender:
                    messages.error(request, f"Sender id ({sender_id}) doesn't exist!")
                    return redirect('transfer_funds')
                if not receiver:
                    messages.error(request, f"Receiver id ({receiver_id}) doesn't exist!")
                    return redirect('transfer_funds')

                if sender_balance < amount:
                    messages.error(request, "Transfer Failed, because The sender balance less than amount")
                    return redirect('transfer_funds')

                sender.balance -= amount
                receiver.balance += amount

                Transactions.objects.create(sender_id=sender_id, receiver_id=receiver_id,
                                            sender_balance_before_transaction=sender_balance,
                                            receiver_balance_before_transaction=receiver_balance, amount=amount)
                sender.save()
                receiver.save()
                messages.success(request, "Transfer completed successfully.")
                return redirect('list_accounts')
        except Exception as e:
            messages.error(request, f"Transfer failed: {e}")
            return redirect('transfer_funds')
    else:
        return render(request, "transfer_funds.html")


def show_history(request, id):
    all_transactions = Transactions.objects.filter(Q(sender_id=id) | Q(receiver_id=id)).order_by('created_at')
    transactions = []
    for transaction in all_transactions:
        if transaction.sender_id == str(id):
            balance = transaction.sender_balance_before_transaction
            amount = f"- {transaction.amount}"
        if transaction.receiver_id == str(id):
            balance = transaction.receiver_balance_before_transaction
            amount = f"+ {transaction.amount}"
        transactions.append({
                "date": transaction.created_at,
                "sender_id":transaction.sender_id,
                "receiver_id":transaction.receiver_id,
                "balance": balance,
                "amount":amount
            })
    return render(request, 'show_history.html', {"transactions": transactions})
