from rest_framework import routers
from createBill.views import CustomerBillViewset

######################### Declare our router #########################
router = routers.SimpleRouter()

######################### Declare our Urls #########################

#### App createBill ####
#/api/createBill/category
router.register('BilltoCustomer', CustomerBillViewset, basename='BilltoCustomer')
