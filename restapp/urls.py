from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('books', BookViewSet, basename='book')

urlpatterns = [
    path('', home , name="home"),
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('', include(router.urls)),
    
]
