from django.test import TestCase
from api.models import Vendor , HistoricalPerformance, PurchaseOrder
from django.urls import reverse

#To run test: ..\Vendor_Management_System_with_Performance_Metrics\VMS> python.exe .\manage.py test -v 2 api/test/
#To run  the test: python manage.py test <app_name>
# Create your tests here.

class VendorModelTestCase(TestCase): #Works
    def setUp(self):
        self.model = Vendor
        # Create a vendor model for testing
        self.vendor_data = {
            "name": "Ash",
            "contact_details": "test contact details of Ash",
            "address": "test address of Ash",
        }
        self.vendor = self.model.objects.create(**self.vendor_data)
        self.vendor_url = self.vendor.get_absolute_url() 
    
    def test_model_instance(self):
        self.assertIsInstance(self.vendor, self.model)
        self.assertEqual(
            str(self.vendor),
            self.vendor_data.get("name"),
            "mismatch model string representation",
        )
    
    def test_model_absolute_url(self):
        expected_model_url = reverse(
            "vendor_detail", kwargs={"pk": self.vendor.pk}
        )
        self.assertEqual(self.vendor_url, expected_model_url, "Invalid url")
    
    
    def test_method_get_purchase_orders_by_status_by_providing_non_status_value(self):
        filter_purchase_orders = self.vendor.get_purchase_orders_by_status(
            status="incomplete"
        )
        self.assertIsNone(filter_purchase_orders)

    def test_calc_on_time_delivery_rate_for_zero_division_error_returned_value(self):
        on_time_delivery_rate = self.vendor.calc_on_time_delivery_rate()
        self.assertEqual(on_time_delivery_rate, 0)

    def test_calc_fulfillment_for_zero_division_error_returned_value(self):
        fulfillment_rate = self.vendor.calc_fulfillment_rate()
        self.assertEqual(fulfillment_rate, 0)

    def test_calc_avg_response_time_returned_value(self):
        avg_response_time = self.vendor.calc_avg_response_time()
        self.assertEqual(avg_response_time, 0)
#end class

class HistoricalPerformanceTestCase(TestCase): #Works
    def setUp(self):
        self.model = HistoricalPerformance
        self.vendor_model = Vendor
        self.vendor_data = {
            "name": "Ash",
            "contact_details": "test contact details of Ash",
            "address": "test address of Ash",
        }
        self.vendor = self.vendor_model.objects.create(**self.vendor_data)

        self.vendor_performance_data = {
            "vendor": self.vendor,
            "on_time_delivery_rate": 95.0,
            "quality_rating_avg": 4.5,
            "average_response_time": 2.5,
            "fulfillment_rate": 98.0,
        }
        self.performance_history = self.model.objects.create(
            **self.vendor_performance_data
        )

    def test_model_instance(self):
        self.assertIsInstance(self.performance_history, self.model)
        
#end class

class PurchaseOrderModelTestCase(TestCase): #works
    def setUp(self):
        self.model = PurchaseOrder
        # Create a vendor model for testing
        self.vendor_data = {
            "name": "Ash",
            "contact_details": "test contact details of Ash",
            "address": "test address of Ash",
        }
        self.vendor = Vendor.objects.create(**self.vendor_data)
        # Create a Purchase Order for testing
        self.po_data = {
            "po_number": "PO12345",
            "order_date": "2023-12-01T08:00:00Z",
            "delivery_date": "2023-12-10T08:00:00Z",
            "items": [{"item_name": "Test Item", "quantity": 5, "unit_price": 10.0}],
            "quantity": 5,
            "status": "pending",
            "quality_rating": None,
            "issue_date": "2023-12-01T08:00:00Z",
            "acknowledgment_date": None,
        }
        self.purchase_order = self.model.objects.create(
            vendor=self.vendor, **self.po_data
        )
        
        self.purchase_order_url = self.purchase_order.get_absolute_url()
        
    def test_model_instance(self):
        self.assertTrue(isinstance(self.purchase_order, self.model))
        self.assertEqual(
            str(self.purchase_order),
            f"{self.purchase_order.po_number} : {self.purchase_order.vendor}",
            "mismatch model string representation",
        )
    
    def test_model_absolute_url(self):
        expected_model_url = reverse(
            "purchase_order_detail", kwargs={"pk": self.purchase_order.pk}
        )
        self.assertEqual(self.purchase_order_url, expected_model_url, "Invalid url")
    
