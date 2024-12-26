from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Book)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['title','author' , 'published_date' , 'isbn','pages','cover','language']