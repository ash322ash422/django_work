from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about', views.AboutView.as_view(), name='about'),
    path('products', views.ProductsView.as_view(), name='products'),
    path('single-product', views.SingleProductView.as_view(), name='single-product'),
    path('contact', views.ContactView.as_view(), name='contact'),
]