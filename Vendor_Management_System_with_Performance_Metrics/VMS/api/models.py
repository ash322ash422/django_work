from django.db import models
from django.utils import timezone
from enum import StrEnum
from typing import Union
import uuid
from django.urls import reverse

class OrderStatus(StrEnum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    
    @classmethod
    def is_valid_status(cls, status: str):
        return status.lower() in [i.name.lower() for i in cls]

#end class

CHOICES_STATUS= (
    (OrderStatus.PENDING,OrderStatus.PENDING),
    (OrderStatus.COMPLETED,OrderStatus.COMPLETED),
    (OrderStatus.CANCELLED,OrderStatus.CANCELLED),
)

def random_code():
    """
    The function `random_code` generates a random code with 12 chars using the UUID library in Python.
    The code returns the last part of a randomly generated UUID.
    """
    return str(uuid.uuid4()).split("-")[-1]
#end def

# Create your models here.
class BaseModel(models.Model):
    """Base Model for Vendor and PurchaseOrder model"""
    id = models.AutoField(primary_key=True, editable=False,) 
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
#end class

class Vendor(BaseModel):
    name =  models.CharField(max_length=50, blank=True, null=True, unique=False,
                help_text="vendors name") 
    contact_details = models.TextField(help_text="Contact information of the vendor") 
    address = models.TextField(help_text="Physical address of the vendor") 
    vendor_code = models.CharField(unique=True, max_length=10,default=random_code, editable=False
                                   ) # A unique identifier for the vendor.
    on_time_delivery_rate = models.FloatField(default=0.0,
                help_text="Tracks the percentage of on-time deliveries") 
    quality_rating_avg = models.FloatField(default=0.0,
                help_text="Average rating of quality based on purchase orders") 
    average_response_time = models.FloatField(default=0.0,
                help_text="Average time taken to acknowledge purchase orders") 
    fulfillment_rate = models.FloatField(default=0.0,
                help_text="Percentage of purchase orders fulfilled successfully") 
    
    class Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"

    def __str__(self):
        return '{}'.format(self.name ,)
    
    def get_absolute_url(self):
        return reverse("vendor_detail", kwargs={"pk": self.pk})

    def get_purchase_orders_by_status(
        self, status=Union[OrderStatus, str] | None
    ) -> models.QuerySet | None:
        
        if status is None:
            return self.purchase_orders.all()
        elif OrderStatus.is_valid_status(status=status):
            return self.purchase_orders.filter(status=status)
        else:
            return None


    def calc_on_time_delivery_rate(self) -> float:
        """
        Return on-time delivery rate that is obtained by dividing the count of purchase orders by
        the count of purchase orders with acknowledgment dates before or on the delivery dates
        """
        po_list = self.get_purchase_orders_by_status(status=OrderStatus.COMPLETED)
        filter_on_time_deliverables = po_list.filter(
            acknowledgment_date__lte=models.F("delivery_date")
        )
        try:
            return round(filter_on_time_deliverables.count() / po_list.count(), 2)
        except ZeroDivisionError:
            return 0


    def calc_avg_quality_ratings(self):
        """
        The function calculates the average quality rating of completed purchase orders
        """
        po_list = self.get_purchase_orders_by_status(status=OrderStatus.COMPLETED)
        result = po_list.aggregate(
            avg_quality_rating=models.Avg("quality_rating", default=0.0)
        )
        return round(result.get("avg_quality_rating"))

    def calc_fulfillment_rate(self):
        """
        The function calculates the fulfillment rate by dividing the number of completed purchase orders
        by the total number of purchase orders
        """
        po_list_status_completed = self.get_purchase_orders_by_status(
            status=OrderStatus.COMPLETED
        )
        po_list = self.get_purchase_orders_by_status(status=None)
        try:
            return round(po_list_status_completed.count() / po_list.count(), 2)
        except ZeroDivisionError:
            return 0

    def calc_avg_response_time(self):
        """
        Return the average response time for purchase orders that have both an issue
        date and an acknowledgment date
        """
        filter_po_data = self.purchase_orders.filter(
            issue_date__isnull=False, acknowledgment_date__isnull=False
        )
        
        if filter_po_data.exists():
            result = filter_po_data.aggregate(
                avg_response_time=models.Avg(
                    models.F("acknowledgment_date") - models.F("issue_date")
                )
            )
            return round(result.get("avg_response_time").total_seconds(), 2)
        else:
            return 0
    
#end class

class PurchaseOrder(BaseModel):
    po_number = models.CharField(unique=True, max_length=10,
                help_text = "Unique number identifying the PO")  
    vendor = models.ForeignKey(to=Vendor, on_delete=models.CASCADE,
                related_name="purchase_orders") 
    order_date = models.DateTimeField(default=timezone.now, 
                help_text = "Date when the order was placed") 
    issue_date = models.DateTimeField(blank=False, default = timezone.now,
                help_text = "Timestamp when the PO was issued to the vendor" ) 
    acknowledgment_date = models.DateTimeField(blank=True, null=True, 
                help_text = "Timestamp when the vendor acknowledged the PO")
    delivery_date = models.DateTimeField(default = timezone.now, 
                help_text = "Expected or actual delivery date of the order")
    quantity = models.IntegerField(default=1, 
                help_text = "Total quantity of items in the PO.") 
    status = models.CharField(choices=CHOICES_STATUS, blank=False, max_length=10,
                default=CHOICES_STATUS[0][0]) # Current status of the PO (e.g., pending, completed, canceled).
    quality_rating = models.FloatField(null=True,blank=True,
                help_text = "Rating given to the vendor for this PO")
    items = models.JSONField(default=dict) # Details of items ordered.
    
    class Meta:
        ordering = ["-order_date"]
        verbose_name = "Purchase Order"
        verbose_name_plural = "Purchase Orders"
    
    def __str__(self):
        return '{} : {}'.format(self.po_number, self.vendor.name)
    
    def get_absolute_url(self):
        return reverse("purchase_order_detail", kwargs={"pk": self.pk})


#end class
    
class HistoricalPerformance(models.Model):
    id = models.AutoField(primary_key=True, editable=False,)
    vendor = models.ForeignKey(to=Vendor, on_delete=models.CASCADE) 
    date = models.DateTimeField(blank=False, default= timezone.now,
        help_text = "Date of the performance record") 
    on_time_delivery_rate = models.FloatField(
        help_text = "Historical record of the on-time delivery rate.")  
    quality_rating_avg = models.FloatField(
        help_text = "Historical record of the quality rating average")
    average_response_time = models.FloatField(
        help_text = "Historical record of the average response time.")
    fulfillment_rate = models.FloatField(
        help_text = "Historical record of the fulfillment rate")
    
    class Meta:
        ordering = ["-date"]
        verbose_name = "Historical Performance"
        verbose_name_plural = "Historical Performances"
        
    def __str__(self):
        return "{} - {}".format(self.vendor.name,self.date)

#end class
