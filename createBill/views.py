from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from createBill.models import Customer_Bill
from createBill.serializers import CustomerBillSerializer



################################### Partie API ###################################

class CustomerBillViewset(ReadOnlyModelViewSet):
    serializer_class = CustomerBillSerializer

    def get_queryset(self):
        # Nous récupérons toutes les factures faites à un client dans une variable nommée queryset
        queryset = Customer_Bill.objects.all()
        # Vérifions la présence du paramètre ‘Customer_Bill_id’ dans l’url et si oui alors appliquons notre filtre
        BilltoCustomer_id = self.request.GET.get('BilltoCustomer_id')
        if BilltoCustomer_id is not None:
            queryset = queryset.filter(BilltoCustomer_id=BilltoCustomer_id)
        return queryset
