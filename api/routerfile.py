from rest_framework import routers
from api.views import CustomerBillViewset

######################### Declare our router #########################
router = routers.SimpleRouter()

######################### Declare our Urls #########################

#### App createBill ####
#/api/BilltoCustomer
router.register('BilltoCustomer', CustomerBillViewset, basename='BilltoCustomer')
