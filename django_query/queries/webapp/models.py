from django.db import models
from  django.utils import timezone
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import Signal, receiver
from datetime import datetime

# Create your models here.
class Query(models.Model ):
    """We do not have to explicitly create Primary Keys b/c auto. does this
    id =models.AutoField(primary_key=True)
    """
    id =models.AutoField(primary_key=True)
    qry_name = models.CharField(max_length = 100, unique = True)
    qry = models.TextField(help_text = 'Enter query here')
    create_by = models.CharField(max_length = 20)
    create_on = models.DateField(verbose_name = "Created 0n", blank=True,
                        null=True, default = timezone.now )
    last_accessed = models.DateTimeField( verbose_name= "Last accessed",
                        help_text = "Last time this query was accessed",
                        blank=True, null=True, default = timezone.now )
    num_visit = models.PositiveIntegerField(verbose_name="Num of visits to this qry", default=1)
    
    def __str__(self):#override
        return "{} by {}".format(self.qry_name, self.create_by,)
    
    #override. This is not recommended. Instead use pre_save/post_save with signals.
    def save(self, *args, **kwargs):
        if len(self.qry_name) < 3:
            #add save logic here
            print("qry_name is small:", self.qry_name)
        super(Query, self).save(*args, **kwargs)
    
    class Meta:
        db_table = 'tb_queries'
        verbose_name = 'Query'
        verbose_name_plural = 'Queries'
        ordering = ['qry_name'] #or use ['-title']

#end class 

@receiver(pre_save, sender=Query)
def get_query_notification(sender, instance, **kwargs):
    print(f"The {instance.qry_name} query was pre_save at {datetime.now()}.")

@receiver(post_save, sender=Query)
def get_query_notification(sender, instance, **kwargs):
    print(f"The {instance.qry_name} query was post_save at {datetime.now()}.")

@receiver(pre_delete, sender=Query)
def get_query_notification(sender, instance, **kwargs):
    print(f"The {instance.qry_name} query delete request was \
        received on {datetime.now()}.")

@receiver(post_delete, sender=Query)
def get_query_notification(sender, **kwargs):
    print(f"The query was deleted successfully on {datetime.now()}.")
    
