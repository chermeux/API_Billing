from rest_framework.serializers import ModelSerializer
from createBill.models import Customer_Bill


class CustomerBillSerializer(ModelSerializer):
    class Meta:
        model = Customer_Bill
        fields = ['id', 'InvoiceNumber', 'CreationDate','InvoiceReason', 'Designations', 'Quantities', 'PriceHT', 'TVA', 'AddInformation']
