from django.contrib import admin
from .models import Query

# Register your models here.
@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    search_fields = ['qry_name','qry']
    list_display = ['id','qry_name','create_by','last_accessed','num_visit']
    ordering = ['qry_name']
    list_filter = ['create_by']
    #list_editable = ['qry_name']
    list_max_show_all = 100
    list_per_page = 50
    show_full_result_count = True
