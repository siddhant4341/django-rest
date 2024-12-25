from django.urls import path,include
from .views import *
urlpatterns = [
    path('', home , name="home"),
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
]
