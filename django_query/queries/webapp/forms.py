from datetime import date
from django import forms
from .models import Query
from  django.forms import ModelForm
from .my_utils import dbg

RADIO_CHOICE = (( '1' , 'Show all results'),
                ('2','Show first 100 results')
               )

qset = Query.objects.all()
create_by_choices = (('c1','choice1'), ('c2','choice2'))

def get_query_choices(qset_tuple):
    qry_name, create_by = qset_tuple
    obj1 = '{}'.format(qry_name)
    obj2 ='{} by {}'.format(qry_name,create_by).replace('_', ' ').title()
    return (obj1, obj2)
    
class QueryForm(forms.Form):
    """ 
    """
    #Override
    def __init__ (self, extra_kwargs=None, *args, **kwargs):#Here we dynamically populate forms
        super(QueryForm, self).__init__( *args,**kwargs)
        query_choices = [('None','--Select Query--' )]
        #dbg("qset=",qset)
        qs_list = qset.values_list('qry_name','create_by')
        qset_temp = list(map(get_query_choices, qs_list)) # list of 2-tuple
        query_choices.extend(qset_temp)
        #dbg("query_choices=",query_choices)
        query_name = forms.ChoiceField(choices=query_choices, label='Choose Query' )
        #query_name = forms.ModelChoiceField(queryset=qset.values_list('qry_name', flat=True), label='Choose Query')
        
        if extra_kwargs: #invoked on POST. User may have changed the query, so read from textbox
            rows = extra_kwargs['query'].count('\n') + 2 #count how many rows are needed in widget
            widget_text_area = forms.Textarea(attrs={'rows':rows, 'cols':50, 'class': 'class_qry','id':'id_qry'})
            query = forms.CharField(label='Query', widget=widget_text_area,initial=extra_kwargs['query'])
            query_id = forms.IntegerField( initial = extra_kwargs ['query_id'] )
        else: #invoked on GET
            query = forms.CharField(label='Query')
            query_id = forms.IntegerField(initial=0)
        
        #self.fields.update(qid = query_id)
        #self.fields.update(qn = query_name)
        #self.fields.update(q= query)
        self.fields.update({'qid' : query_id, 'qn' : query_name, 'q' : query})
        query_opt = forms.ChoiceField(label='Choose an option',widget=forms.RadioSelect,
                                      choices = RADIO_CHOICE, initial = '1')
        self.fields.update(qo=query_opt)
        #dbg("self.fields=",self.fields)
        
#end class


class AddQueryForm(forms.Form):
    #override
    def __init__(self, *args,  **kwargs): #dynamically populate fields
        super(AddQueryForm, self).__init__(*args, **kwargs)
        
        query_name = forms.CharField(label='Query Name',
                                     help_text='Enter query name here. Try to be descrtptive here')
        create_by = forms.CharField(label='Created By')
        widget_text_area = forms.Textarea(attrs= {'rows': 20, 'cols': 100,})
        query =forms.CharField(label='Query', widget = widget_text_area)
    
        self.fields.update(query_name = query_name)
        self.fields.update(create_by = create_by)
        self.fields.update(query = query)
  
##end class
    
# #NOTE: Following works too
# class AddQueryForm(ModelForm):
#     class Meta:
#         model = Query
#         fields = ['qry_name', 'create_by','qry']
        
# #end class

# class DuplicatesForm(Forms.Form):
#     #0verride
#     def __init__(self,extra_kwargs=None, *args , **kwargs ): #tHere we dynamically populate form
#         super(DuplicatesForm, self). __init__( *args ,**kwargs )
#         if extra_kwargs:#invoked on POST. User may have changed the query, so read from textbox.
#             days_go_back = forms.IntegerField( initial=extra_kwargs['days_go_back'],
#                                               label="Type how many days you want to go back to check duplicates."
#                                              )
#         else: #invoked on GET
#             days_go_back = forms.IntegerField(initial=90,
#                                               label="Type how many days you want to go back to check duplicates.")
#         self.fields.update(days_go_back = days_go_back)
# #enc class 

