from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from createBill.models import Customer_Bill
from api.serializers import CustomerBillSerializer
from rest_framework.permissions import IsAuthenticated


class CustomerBillViewset(ReadOnlyModelViewSet):#(MultipleSerializerMixin, ModelViewSet) #TODO mettre ça pour utiliser tout le CRUD
    serializer_class = CustomerBillSerializer
    #TODO voir si no²us ne devons pas rajouter plus d'élements comme une authentification que pour un certain genre de personnes
    #permission_classes = [IsAuthenticated]#TODO mettre ça pour autoriser le CRUD juste aux personnes identifiées

    def get_queryset(self):
        #TODO ATTENTION SECURITE - ici nous récupérons tous les factures, mais faudra récupérer que les factures faites par un client donc ne pas utiliser all
        #Store all a customer's invoices in queryset
        queryset = Customer_Bill.objects.all()

        #check for the presence of the id parameter in the url
        BilltoCustomer_id = self.request.GET.get('id')
        if BilltoCustomer_id is not None:
            queryset = queryset.filter(id=BilltoCustomer_id)

        #check for the presence of the InvoiceNumber parameter in the url
        BilltoCustomer_InvoiceNumber = self.request.GET.get('InvoiceNumber')
        if BilltoCustomer_InvoiceNumber is not None:
            queryset = queryset.filter(InvoiceNumber=BilltoCustomer_InvoiceNumber)

        # check for the presence of the InvoiceReason parameter in the url
        BilltoCustomer_InvoiceReason = self.request.GET.get('InvoiceReason')
        if BilltoCustomer_InvoiceReason is not None:
            queryset = queryset.filter(InvoiceReason=BilltoCustomer_InvoiceReason)

        # check for the presence of the CreationDate parameter in the url
        BilltoCustomer_CreationDate = self.request.GET.get('CreationDate')
        if BilltoCustomer_CreationDate is not None:
            queryset = queryset.filter(CreationDate=BilltoCustomer_CreationDate)
        return queryset
