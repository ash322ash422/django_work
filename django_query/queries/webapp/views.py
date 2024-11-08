from django.shortcuts import render, redirect;
from django.http import Http404, HttpResponse, FileResponse
from django.views.generic import ListView
from .forms import QueryForm , AddQueryForm
import pandas as pd;
import sys, os
#from cx_Oracle import makedsn, connect;
from django.forms import FilePathField
from .models import Query
from django.urls import reverse
from django.views.generic.edit import FormView
from django.utils import timezone
from .my_utils import dbg
from queries.settings.base import BASE_DIR
from django.contrib import messages

# Create your views here.
#BASE_DIR = os.getcwd()

def get_df_ORIG(qry):
    dsn = makedsn( '132,10,10.205', '1521', 'idoc')
    connection = connect('lw', 'green', dsn)
    pd.set_option( 'display.width', 120, 'max_colwidth', 150) #display.width changes stdout-display
    msg = ""
    try: 
        df = pd.read_sql_query(sql=qry, con = connection)
        connection.close( )
    except pd.io.sql.DatabaseError:
        print("sys.exc_info()=",sys.exc_info())
        df = pd.DataFrame()
        msg = "Invalid query:" + str(sys.exc_info()[1])

    return (df,  msg)
#end def

def get_df(qry):
    #error_msg = "Executed " + qry[0:100]
    error_msg = ""
    WORK_DIR = BASE_DIR.parent / 'webapp'
    df = pd.read_csv(WORK_DIR / "employees.csv")
    
    return (df, error_msg)
#end def


class QueryView(ListView):
    template_name = "webapp/query.html"
    
    def get(self,*args,**kwargs): #override
        form = QueryForm() 
        #dbg("form=",form)
        #dbg("form.fields['qn']=", form.fields['qn'])
        
        context = {'form': form}
        return render (self.request, self.template_name, context)
    
    def post(self, *args, **kwargs):
        #dbg("self.request.POST=",self.request.POST)    
        try:
            qry_opt = self.request.POST['qo']
        except:
            qry_opt = None
        
        #Find query name base on qid:
        #obj = Query.objects.filter(qid=self.request.POST['qid']).first()
        #print("o=",o.qry_name)
        #qry_name = obj.qry_name
        #qry_name = "test"
        qry_name = self.request.POST['qn']
        #result_obj = Query.objects.get(id=pk)
        
        result_obj = Query.objects.filter(qry_name__icontains = qry_name).first()
        #dbg("result_obj=",result_obj)
        num_visits = ''
        last_accessed = ''
        if result_obj != None:
            qry_id = result_obj.id
            qry = result_obj.qry
            num_visits = result_obj.num_visit
            last_accessed = result_obj.last_accessed
            result_obj.num_visit = num_visits + 1
            result_obj.last_accessed = timezone.now()
            result_obj.save()
        else: #This is the user edited query that is read from textbox
            #dbg("self.request.POST['q']=",self.request.POST['q'])
            qry = self.request.POST['q']
            try:
                qry_id = self.request.POST['qid']
            except:
                qry_id = None
        #end if-else
        
        extra_kwargs = {'query':qry, 'query_id': qry_id}
        form = QueryForm(extra_kwargs)
        (df,error_msg) = get_df(qry)
        
        if qry_opt == '2':
            df = df.head(100)
        if len(df) > 10000:
            raise Http404("Your query returned " + str(len(df)) + " results. Your query should return \
                no more than 10,000 records. Either filter your query or press 'DOWNLOAD' to \
                    download ALL results")
        
        if df.empty:
            count = 0
            df_html = "No records"
        else:
            count = len(df)
            df.index = range(1,len(df) + 1)
            df_html = df.to_html()
        
        message = str(count) + " records found."
        context = { 'form': form,'message': message, 
            'error_msg':error_msg,'df_html': df_html,
            'qry_name' :qry_name, 'num_visits': num_visits,
            'last_accessed': last_accessed,
        }
        return render(self.request, 'webapp/query_results.html', context )
        
#end Class

class DownLoadQueryView(ListView): #WORKS
    def post(self ,*args, **kwargs):#override
        qry_name = self.request.POST['qn']
        result_obj = Query.objects.filter(qry_name__icontains = qry_name).first()
        
        num_visits = ''
        last_accessed = ''
        if result_obj != None:
            qry_id = result_obj.id
            qry = result_obj.qry
            num_visits = result_obj.num_visit
            last_accessed = result_obj.last_accesséd
            result_obj.num_visit = num_visits + 1;
            result_obj.last_accessed = timezone.now()
            result_obj.save()
        else: #this is the user edited query that is read from Textbox
            qry = self.request.POST['q']
            try:
                qry_id = self.request.POST['qid']
            except:
                qry_id = None
        #end if-else
        
        (df,error_msg) = get_df(qry)
        if len(error_msg) > 2:
            raise Http404("ERRRAROR in query: " + error_msg)
        df.index = range(1, len(df)+1)
        
        filename = BASE_DIR.parent / 'webapp' / "query_temp.xlsx"#NOTE make it writeable recursively
        df.to_excel( filename, startrow=0, sheet_name="sheet1")#generates excel file in CWO
        
        response = FileResponse(open(filename, 'rb'))
        response['Content-Disposition'] = 'attachment; filename={}'.format("query_temp.xlsx" )
        return response
#end class

class SaveChangesQueryView(ListView):
    template_name = "webapp/query.html"
    
    def post(self, *args, **kwargs ): #override
        
        qry_id = self.request.POST['qid']
        result_obj = Query.objects.get(id=qry_id)
        qry_name = result_obj.qry_name
        qry_new = self.request.POST['q']
        qry_orig = result_obj.qry
        result_obj.qry = qry_new
        result_obj.save()
        msg = "Successfully changed query_name=" + qry_name + "<p> orginal query= " \
            + qry_orig.replace( '\n', '<br />') + "<br />to new query=" + qry_new.replace('\n', '<br />')
        form = QueryForm()
        context = {'form': form, 'message': msg}
        return render(self.request, self.template_name, context )
 #end class
 
class AddQueryView(FormView):
    template_name = "webapp/add_query_form.html"
     
    def get(self,*args,**kwargs): #override
        form = AddQueryForm()
        context = { 'form': form }
        return render(self.request, self.template_name, context )
    #end def
      
    def post(self,*args,**kwargs): #override
        form = AddQueryForm(self.request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            qry_name = formdata['query_name'].lower()
            create_by = formdata['create_by'].lower()
            qry = formdata['query']
            last_accessed = timezone.now()
            obj, created = Query.objects.update_or_create(qry_name = qry_name, qry = qry,
                                create_by = create_by,create_on = last_accessed,
                                last_accessed = last_accessed, defaults={'num_visit': 1},
                            )
            messages.add_message(self.request, messages.INFO, "Successfully added query: " + qry_name)
            return redirect(reverse('webapp:query'))
        else:
            return Http404("form is invalid")
    #end def
#end class

class AllQueryView(ListView): #WORKS
    model = Query
    #template name = “webapp/workqueries_list. html” #Template used to render and should be present.
    def get_context_data(self, **kwargs):#override, This is not really needed for rendering.
        context = super(AllQueryView, self).get_context_data(**kwargs)
        context['now'] = timezone.now( )# NOTE: more keys can he added here,
        for o in self.object_list:#prettify it
            #dbg("o=",o)
            o.qry = str(o.qry).replace('\n','<br />')
        return context
#end class



