from django.dispatch import Signal, receiver
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete #EXTRA
from .models import HistoricalPerformance, Vendor
from  .my_utils import dbg
import inspect 

# Define signals for calculating vendor performance metrics based changes in
# purchase order status.
po_acknowledged_signal = Signal()
po_status_completed_signal = Signal()

@receiver(signal = po_acknowledged_signal)
def update_avg_response_time(sender, instance, **kwargs):
    vendor = instance.vendor
    vendor.average_response_time = vendor.calc_avg_response_time()
    vendor.save()
    
    return vendor
#end def

@receiver(signal = po_status_completed_signal)
def update_performance_metrics(sender, instance, **kwargs):
    vendor = instance.vendor
    #dbg("..inside ",inspect.currentframe().f_code.co_name)
    
    #compute metrics
    on_time_delivery_rate = vendor.calc_on_time_delivery_rate()
    quality_rating_avg = vendor.calc_avg_quality_ratings()
    fulfillment_rate = vendor.calc_fulfillment_rate()

    # dbg("..before:on_time_delivery_rate=",vendor.on_time_delivery_rate,
    #     ";quality_rating_avg=",vendor.quality_rating_avg,
    #     ";fulfillment_rate",vendor.fulfillment_rate)
   
    #update vendor metrics
    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.quality_rating_avg = quality_rating_avg
    vendor.fulfillment_rate = fulfillment_rate
    vendor.save()
    vendor.refresh_from_db()
    
    # dbg("..after:on_time_delivery_rate=",vendor.on_time_delivery_rate,
    #     ";quality_rating_avg=",vendor.quality_rating_avg,
    #     ";fulfillment_rate",vendor.fulfillment_rate)

    # create historical performance
    historical_performance_model = HistoricalPerformance
    historical_performance_model.objects.create(
        vendor=vendor,
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg,
        fulfillment_rate=fulfillment_rate,
        average_response_time=vendor.average_response_time,
    )
    return vendor
#end def

#####################################################
#Following is extra work:
#Pre_save is provoked just before the model save() method is called. 
# This is called when vendor is updated via admin interface or serializer 
@receiver(pre_save, sender=Vendor) 
def notify_before_vendor_name_save(sender, instance, ** kwargs): #works

    # If instance/row is being created, then do nothing
    if instance.id is None:
        pass

    # Else if it is being modified
    else:
        current = instance
        previous = Vendor.objects.get(id=instance.id)

        # If previous reaction is not equal to the current reaction
        if previous.name != current.name:
            # notify instance.article.author
            #print(f".. inside {inspect.currentframe().f_code.co_name}. Name of vendor \
            #    {previous.name} is being changed")
            pass # NOTE: Enable this when needed by removing this pass stmt
#end def

#post_save is provoked just after the model save() method is called. 
# This is called when vendor is created via admin interface or serializer 
@receiver(post_save, sender=Vendor)
def notify_after_vendor_creation(sender, instance, created, ** kwargs) :
    if created:
        print(f".. inside {inspect.currentframe().f_code.co_name}. Creating vendor {instance.name}")
#end def

#pre_delete is provoked just before the model delete() method is called. 
# This is called when vendor is deleted via admin interface or serializer 
@receiver(pre_delete, sender=Vendor)
def notify_before_vendor_deletion(sender, instance, origin, ** kwargs) :
    print(f".. Deleting vendor instance {instance} with origin {origin}")
#end def

#post_delete is provoked just after the model delete() method is called. 
# This is called when vendor is deleted via admin interface or serializer 
@receiver(pre_delete, sender=Vendor)
def notify_after_vendor_deletion(sender, instance, origin, ** kwargs) :
    print(f".. Deleting vendor instance {instance} with origin {origin}")

