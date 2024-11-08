from django.contrib import admin
from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address, UserProfile

# Register your models here.

#Create personalized admin page
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon'
                    ]
    list_display_links = [
        'user',
        'shipping_address',
        'billing_address',
        'payment',
        'coupon'
    ]
    list_filter = ['ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted'
                   ]
    search_fields = [
        'user__username',
        'ref_code'
    ]

    def action_make_refund_accepted(modeladmin, request, queryset):
      queryset.update(refund_requested=False, refund_granted=True)
    #end def
    action_make_refund_accepted.short_description = 'Update orders to refund granted'
    actions = [action_make_refund_accepted]
#end class

#Create personalized admin page
class AddressAdmin(admin.ModelAdmin):
    list_display = [ 'user','street_address', 'apartment_address', 'country','zip',
                     'address_type', 'default'
                   ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']
#end class

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile)
