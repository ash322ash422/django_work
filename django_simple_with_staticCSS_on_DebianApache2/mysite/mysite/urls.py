from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('notes.urls', namespace='notes')),
    path('blog/', include('blog.urls')),
]



#The following was added to see CSS,etc files during production.
if not settings.DEBUG:
  urlpatterns = urlpatterns + [
    
    #re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
  ]


