from django.contrib import admin
from .models import Vendor, PurchaseOrder, HistoricalPerformance

# Register your models here.
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin ):
    search_fields = ["name", "vendor_code"]
    list_display = ["id","vendor_code","name","contact_details","address", 
                    "on_time_delivery_rate", "quality_rating_avg",
                    "average_response_time",
               ]
    ordering = ['name']
    list_display_links = ['vendor_code']
    #list_filter = []
    list_editable = ['name']
    #list_max_show_all = 100
    list_per_page = 50
    show_full_result_count = True
#end class

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin ):
    search_fields = ["vendor","items" ]
    list_display = [ "id","po_number","vendor",
                     "order_date",
                     "issue_date",
                     "acknowledgment_date",
                     "delivery_date",
                     "quantity",
                     "status",
                     "quality_rating",
                     "items"
                   ]
    ordering = ['vendor']
    #list_filter = ['status']
    #list_editable = ['status']
    list_per_page = 50
    show_full_result_count = True
#end class

@admin.register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin ):
    search_fields = ["vendor", ]
    list_display = ["vendor","date","on_time_delivery_rate",
                    "quality_rating_avg","average_response_time",
                    "fulfillment_rate"
                   ]
    ordering = ['vendor']
    #list_filter = ['status']
    #list_editable = ['status']
    list_per_page = 50
    show_full_result_count = True
#end class
    