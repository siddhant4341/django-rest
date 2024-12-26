from  rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
# Create your views here.

@api_view(['GET', 'POST','PATCH'])
def home(request):
    if request.method == "GET":
        return Response({
            'status':200,
            'message':'django rest framework is running..',
            'method_called':'you called GET method'
        })
    elif request.method == "POST":
        return Response({
            'status':400,
            'message':'django rest framework is running..',
            'method_called':'you called POST method'
        })
    elif request.method == "PATCH":
        return Response({
            'status':600,
            'message':'django rest framework is running..',
            'method_called':'you called PATCH method'
        })
    
    else:
        return Response({
            'status':200,
            'message':'django rest framework is running..',
            'method_called':'you called INVALID method'
        })
    


class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




    
    '''def student_api(request):
        if request.method == 'GET':
            json_data = request.body
            stream = io.ByteIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id',None)
            if id is not None:
                stu = Student.objects.get(id = id)
                serializer = StudentSerializer(stu)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data,  content_type='application/json')'''
        


    
