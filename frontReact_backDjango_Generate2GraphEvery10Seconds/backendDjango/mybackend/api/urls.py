from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataViewSet

router = DefaultRouter()
router.register(r'data', DataViewSet)

#GET http://127.0.0.1:8000/api/data/
#GET http://127.0.0.1:8000/api/data/random_variation/

urlpatterns = [
    path('', include(router.urls)),
]