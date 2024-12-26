
from django.contrib import admin
from django.urls import path,include
from restapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include('restapp.urls')),
    
]
