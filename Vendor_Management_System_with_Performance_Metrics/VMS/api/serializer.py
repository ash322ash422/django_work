from rest_framework import serializers
from django.utils import timezone
from django.utils.translation import gettext as _
from  .models import (Vendor,
                      PurchaseOrder,
                      OrderStatus,
                      )
from .my_signals import ( po_acknowledged_signal,
                          po_status_completed_signal,
                        )

class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = "__all__"
        # We CANNOT perform UPDATE on read_only_fields via endpoints. Also, if these fields are
        # specified during CREATE, then they are ignored.
        read_only_fields = [ #Works.
            "id",
            "vendor_code",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = { #This works
            "name": {
                "error_messages": {
                    "required": _("PPlease provide name of vendor. This is required field")
                }
            },
            "contact_details": {
                "error_messages": {
                    "required": _("PPlease provide vendor contact details. This is required field")
                }
            },
            "address": {
                "error_messages": {
                    "required": _("PPlease provide vendor address. This is required field")
                }
            },
        }
#end class

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]
#end class

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        #Only these fields are going to be updated through serializer. Other updated fields
        # would be ignored by serializer.
        fields = '__all__'
        
    def update(self, instance, validated_data):
        """ Here we update the attr.(AKA fields) of instance object. The attr and its value 
        is obtained from validated_data dict. 
        """
        #For an 'instance' object, set the 'value' of an 'attr' dynamically at runtime. 
        # The 'instance' is instance of class PurchaseOrder model
        for attr, value in validated_data.items():
            #Here we update all attr(like vendor, issue_date, acknowledgement_date,etc) of 
            # an instance object.The attr and value is obtained from validated_data. The 
            # attr are from 'fields' defined above.
            setattr(instance, attr, value)
        instance.save()
        if instance.status == OrderStatus.COMPLETED:
            po_status_completed_signal.send(
                sender=instance.__class__, instance=instance
            )
        return instance
#end class

class PurchaseOrderAcknowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        #Only below field is going to be processed/updated through serializer. 
        # Other fields would be ignored by serializer.
        fields = ["acknowledgment_date",] 
        extra_kwargs = {"acknowledgment_date": {"required": True}}

    #override#NOTE: This method is always named as validate_<field_name>
    def validate_acknowledgment_date(self, value): 
        """
        Check that the acknowledgment_date is correct
        """
        if not value:
            value = timezone.now()
        return value

    #override: #This is called by performed_update method inside generics.UpdateAPIView
    def update(self, instance, validated_data): 
        """ 
        Here we update the attr.(i.e. acknowledgement_date) of instance object. The attr and
        its value is obtained from validated_data dict. 
        """
        #For an 'instance' object, set the 'value' of an 'attr' dynamically at runtime. 
        # The 'instance' is instance of class PurchaseOrder model
        #NOTE: There is going to be only 1 attr, acknowledgement_date
        for attr, value in validated_data.items(): 
            #Here only 1 attr(acknowledgement_date) value is being set for the PO instance
            setattr(instance, attr, value) 
        instance.save()
        
        po_acknowledged_signal.send(sender=instance.__class__,
                                    instance=instance )
        
        return instance
#end class
