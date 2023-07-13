from django.db import models
from datetime import datetime

class Customer_Bill(models.Model):
    id = models.AutoField(primary_key=True)
    InvoiceNumber = models.CharField(null=True, max_length=100)
    CreationDate = models.DateField(default=datetime.now(), blank=True)
    InvoiceReason = models.CharField(null=True, max_length=100)
    Designations = models.TextField(null=True)
    Quantities = models.TextField(null=True)
    PriceHT = models.TextField(null=True)
    TVA = models.TextField(null=True)
    AddInformation = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.InvoiceNumber

