# Generated by Django 4.2.3 on 2023-07-16 00:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createBill', '0005_customer_bill_creationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_bill',
            name='CreationDate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 7, 16, 2, 27, 57, 261990)),
        ),
    ]
