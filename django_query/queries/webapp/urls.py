from django.urls import path
from . import views

app_name = 'webapp'
urlpatterns = [
    path("", views.QueryView.as_view(), name="query"),
    path("download/", views.DownLoadQueryView.as_view(), name="download_query"),
    path("save_query/", views.SaveChangesQueryView.as_view(), name="save_changes_query"),
    path("all_query_list/", views.AllQueryView.as_view(), name="all_query_list"),
    path("add_query/", views.AddQueryView.as_view(), name="add_query"),
    
]