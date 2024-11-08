from django.contrib import admin
from django.urls import path
from  emailapp.views import EmailView, EmailManyView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", EmailView.as_view()),
    path("send_mass_email/", EmailManyView.as_view()),
    
]
