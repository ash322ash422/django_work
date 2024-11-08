from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("appmain.urls")),
    #path("appmain/", include("appmain.urls")),
    
]

#The following was added to see CSS,etc files during production.
if not settings.DEBUG:
  urlpatterns = urlpatterns + [
    
    #re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
  ]




