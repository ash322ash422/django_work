from django.contrib import admin
from django.urls import path
from fruits import views
from  rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fruits/', views.fruit_list),
    path('fruits/<int:id>',views.fruit_detail)
]

# NOTE: I had to add allowed arg to get it working for both 
# 'http://127.0.0.1:8000/fruits.json' and 'http://127.0.0.1:8000/fruits'
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])