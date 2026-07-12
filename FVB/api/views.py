from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def Hello(request):
    return Response({'message': 'Hello, World!'})

@api_view(['POST'])
def hello_post(request):
    if request.method == 'POST':
        print(request.data)
        return Response({'message': 'Hello, POST!'})
    
@api_view(['GET', 'POST'])  
def hello_get_post(request):
    if request.method == 'GET':
        return Response({'message': 'Hello, GET!'})
    elif request.method == 'POST':
        print(request.data)
        return Response({'message': 'Hello, POST!'})  