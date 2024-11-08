from rest_framework import serializers
from webapp.models import Query
from webapp.my_utils import dbg
from .signals import query_updated_signal
from django.utils.translation import gettext as _
#from rest_framework.validators import ValidationError

class QuerySerializer(serializers.ModelSerializer): #NOTE: This does not have delete method
    qry_name = serializers.CharField(max_length=100)
    
    def validate(self, data): ##override. Invoked on CREATE,UPDATE.
        """
        Validate the data
        """
        if len(data['qry_name']) < 3:
            raise serializers.ValidationError({'errorrr': 'qry_name is too short.'}) 
        return data
    
    def create(self, validated_data):#override. Invoked on CREATE
        """
        Create and return a new `Query` instance, given the validated data.
        """
        dbg("inside QuerySerializer.create")
        dbg("..validated_data=",validated_data)
        
        return Query.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data): #override. Called on UPDATE
        dbg("inside QuerySerializer.update")
        dbg("..instance=",instance)
        dbg("..validated_data=",validated_data)
        
        #Now we update the instance with validated data
        for attr, value in validated_data.items():
           setattr(instance, attr, value)
        
        instance.save()
        #instance.refresh_from_db() #refresh the instance
        
        if (instance.create_by).lower() == "ash": #signal generated when ash creates a query
            data = {"msg":"message goes here"}
            query_updated_signal.send(sender = instance.__class__, instance = instance, data = data )
        
        return instance
         
    class Meta:
        model = Query
        fields = ['qry_name','qry','create_by','create_on','last_accessed']
             