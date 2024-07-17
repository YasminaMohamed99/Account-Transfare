# Generated by Django 5.0.7 on 2024-07-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Accounts",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("balance", models.DecimalField(decimal_places=10, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Transactions",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("sender_id", models.CharField(max_length=255)),
                ("receiver_id", models.CharField(max_length=255)),
                ("amount", models.DecimalField(decimal_places=10, max_digits=10)),
            ],
        ),
    ]