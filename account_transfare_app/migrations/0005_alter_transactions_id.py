# Generated by Django 5.0.7 on 2024-07-19 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_transfare_app', '0004_transactions_receiver_balance_before_transaction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
