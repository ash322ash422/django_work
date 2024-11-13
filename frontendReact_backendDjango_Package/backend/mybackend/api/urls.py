from django.urls import path
from . import views_plot, views_playground, views_GET_POST_upload_download
from .views_upload import FileUploadView
from .views_z1_data import Z1DataView

urlpatterns = [
    path('playground/', views_playground.play_json_response, name='playground'), #for testing
    path('get-z1-data/', Z1DataView.as_view(), name='get_z1_data'),
    
    path('get-data/', views_GET_POST_upload_download.get_data, name='get_data'),
    path('post-data/', views_GET_POST_upload_download.post_data, name='post_data'),
    path('upload-file_1/', views_GET_POST_upload_download.upload_file, name='upload_file_1'),
    path('download-file/<str:filename>/', views_GET_POST_upload_download.download_file, name='download_file'),
    
    
    path('upload-file/', FileUploadView.as_view(), name='upload-file'),
    path('plot/', views_plot.plot, name='plot'),
    
    path('plot-data/', views_plot.get_plot_data, name='plot-data'),
    
]

