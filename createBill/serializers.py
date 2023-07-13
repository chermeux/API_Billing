from rest_framework.serializers import ModelSerializer
from .models import Customer_Bill


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Customer_Bill
        fields = ['id', 'InvoiceNumber', 'CreationDate','InvoiceReason', 'Designations', 'Quantities', 'PriceHT', 'TVA', 'AddInformation']
