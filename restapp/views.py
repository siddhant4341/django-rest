from  rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *
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
