from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.
class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        print("*************List*****************")
        print("Basename :" ,self.basename)
        print("Action :" ,self.action)
        print("Detail :" ,self.detail)
        print("Suffix :" ,self.suffix)
        print("Name :" ,self.name)
        print("Description :" ,self.description)
        stu=Student.objects.all()
        serliazed=StudentSerializer(stu,many=True)
        return Response(serliazed.data)
    
    def retrieve(self,request,pk):
        print("*************Retrieve*****************")
        print("Basename :" ,self.basename)
        print("Action :" ,self.action)
        print("Detail :" ,self.detail)
        print("Suffix :" ,self.suffix)
        print("Name :" ,self.name)
        print("Description :" ,self.description)
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serliazed=StudentSerializer(stu)
            return Response(serliazed.data)
        return Response({'msg':"Record Not Found!"})
    
    def create(self,request):
        print("*************Create*****************")
        print("Basename :" ,self.basename)
        print("Action :" ,self.action)
        print("Detail :" ,self.detail)
        print("Suffix :" ,self.suffix)
        print("Name :" ,self.name)
        print("Description :" ,self.description)
        serialized=StudentSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response({'msg':"Data Creted"})
        return Response({'msg':"Data not  Creted"})
    
    def update (self,request,pk):
        print("*************update*****************")
        print("Basename :" ,self.basename)
        print("Action :" ,self.action)
        print("Detail :" ,self.detail)
        print("Suffix :" ,self.suffix)
        print("Name :" ,self.name)
        print("Description :" ,self.description)
        id=pk
        stu=Student.objects.get(id=id)
        serliazed=StudentSerializer(stu,data=request.data)
        if serliazed.is_valid():
            serliazed.save()
            return Response({'msg':"Data Updated"})
        return Response({'msg':"Data not  updated"})
    
    def partial_update (self,request,pk):
        print("*************partial_update*****************")
        print("Basename :" ,self.basename)
        print("Action :" ,self.action)
        print("Detail :" ,self.detail)
        print("Suffix :" ,self.suffix)
        print("Name :" ,self.name)
        print("Description :" ,self.description)
        id=pk
        stu=Student.objects.get(id=id)
        serliazed=StudentSerializer(stu,data=request.data,partial=True)
        if serliazed.is_valid():
            serliazed.save()
            return Response({'msg':"Data Updated"})
        return Response({'msg':"Data not  updated"})

    def destroy(self,request,pk):
        print("*************Destroy*****************")
        print("Basename :" ,self.basename)
        print("Action :" ,self.action)
        print("Detail :" ,self.detail)
        print("Suffix :" ,self.suffix)
        print("Name :" ,self.name)
        print("Description :" ,self.description)
        id=pk
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})


    
