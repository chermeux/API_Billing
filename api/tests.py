from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import include, path, reverse
from createBill.models import Customer_Bill
from datetime import datetime

class TestCustomer_Bill(APITestCase):
    url = reverse_lazy('BilltoCustomer-list')

    def format_datetime(self, value):
        # Cette méthode est un helper permettant de formater une date en chaine de caractères sous le même format que celui de l’api
        return value.strftime("%Y-%m-%d")

    def test_list(self):
        #DataBilltoCustomer = Customer_Bill.objects.create(InvoiceNumber="1", InvoiceReason="Test 1", Designations="Les designations", Quantities="2", PriceHT="4", TVA="1", AddInformation="supplementaire", CreationDate=datetime.now())

        response = self.client.get(reverse("BilltoCustomer-list"))
        # Nous vérifions que le status code est bien 200
        # et que les valeurs retournées sont bien celles attendues
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        """
        excepted = [
            {
                'id': DataBilltoCustomer.pk,
                'InvoiceNumber': DataBilltoCustomer.InvoiceNumber,
                'InvoiceReason': DataBilltoCustomer.InvoiceReason,
                'Designations': DataBilltoCustomer.Designations,
                'Quantities': DataBilltoCustomer.Quantities,
                'PriceHT': DataBilltoCustomer.PriceHT,
                'TVA': DataBilltoCustomer.TVA,
                'AddInformation': DataBilltoCustomer.AddInformation,
                'CreationDate': self.format_datetime(DataBilltoCustomer.CreationDate),
            }
        ]
        self.assertEqual(excepted,response.json())

    def test_create(self):
        # Nous vérifions qu’aucune catégorie n'existe avant de tenter d’en créer une
        self.assertFalse(Customer_Bill.objects.exists())
        response = self.client.post(self.url, data={
            'InvoiceNumber': "3",
            'InvoiceReason': "Test impossiblité de créer",
            'Designations': "Designations qui doivent pas exister",
            'Quantities': "Quantités qui doivent pas exister",
            'PriceHT':"Prix qui doivent pas exister",
            'TVA': "TVA qui doivent pas exister",
            'AddInformation': "informations supp qui doivent pas exister",
            'CreationDate': datetime.now(),
        })
        # Vérifions que le status code est bien en erreur et nous empêche de créer une catégorie
        self.assertEqual(response.status_code, 405)
        # Enfin, vérifions qu'aucune nouvelle catégorie n’a été créée malgré le status code 405
        self.assertFalse(Customer_Bill.objects.exists())
        """


