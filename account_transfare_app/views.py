import uuid
import pandas as pd
from django.shortcuts import render
from account_transfare_app.forms import UploadFileForm
from account_transfare_app.models import Accounts


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
                
            for _, row in df.iterrows():
                account_id = uuid.UUID(row['ID'])
                account, created = Accounts.objects.get_or_create(id=account_id, defaults={'name': row['Name'],
                                                                                           'balance': row['Balance']})
                if not created:
                    account.name = row['Name']
                    account.balance = row['Balance']
                    account.save()
    else:
        form = UploadFileForm()

    return render(request, 'list_accounts.html', {'form': form})
