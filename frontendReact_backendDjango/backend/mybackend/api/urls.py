from django.urls import path
from . import views
from .views_up_down_load import FileUploadView, FileDownloadView
from .views_graph_plotly  import Z1DataView

urlpatterns = [
    path('get-data/', views.get_data, name='get_data'),
    path('post-data/', views.post_data, name='post_data'),
    
    path('upload-file/', FileUploadView.as_view(), name='file-upload'), #TODO add views_..
    path('download-file/<str:filename>/', FileDownloadView.as_view(), name='file-download'),
    
    path('get-z1-data/', Z1DataView.as_view(), name='get-z1-data'),
]

