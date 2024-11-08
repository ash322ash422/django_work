from django.dispatch import Signal, receiver
from webapp.models import Query
from  webapp.my_utils import dbg

# Define signals 
query_updated_signal = Signal()

@receiver(signal = query_updated_signal)
def signal_handler(sender, instance, **kwargs):
    dbg("inside signal_handler. Query is being updated. Sending signal")
    dbg("..sender=",sender)
    dbg("..instance=",instance)
    dbg("..kwargs=",kwargs)
    qry_name = instance.qry_name
    print("signal handler called with query=",qry_name)

#####################################################

