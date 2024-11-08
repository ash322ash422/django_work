from django import template
from store.models import Order
#This file needs to be present here ()../templates/cart_template_tags.py)
# for {% load cart_template_tags %}, which is in navbar.html, to work
register = template.Library()

@register.filter
def cart_item_count(user): # invoked as {{ request.user|cart_item_count }} inside navbar.html
    if user.is_authenticated:
      qs = Order.objects.filter(user=user, ordered=False)
      if qs.exists():
        return qs[0].items.count()
    return 0
