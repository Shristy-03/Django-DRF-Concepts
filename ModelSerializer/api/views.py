from django.shortcuts import render

# Create your views here.
import io
from django.http import JsonResponse
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser

from .models import Student
from .serializers import StudentSerializer    
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# create operation
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            return JsonResponse(res, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

# read operation
def student_detail(request):    
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data, status=200)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)    
@csrf_exempt
def student_update(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated'}
            return JsonResponse(res, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)        

@csrf_exempt
def stu_delete(request):
    if request.method=="DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'Data Deleted'}
        return JsonResponse(res, status=200)
    

