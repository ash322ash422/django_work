from django.contrib import admin
from django.urls import path
from fkey import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/book/', views.book_list),
    path('api/book/<int:id>',views.book_detail),

    path('api/author/', views.author_list),
    path('api/author/<int:id>',views.author_detail),

    #path('watch/stream/', views.watch_list),
]
