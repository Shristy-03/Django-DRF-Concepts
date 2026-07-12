from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Student created successfully'}, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self,request,pk,format=None):
        student_id = pk
        student = Student.objects.get(id=student_id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Student updated successfully'})
        return Response(serializer.errors, status=400)
    
    def patch(self,request,pk,format=None):
        student_id = pk
        student = Student.objects.get(id=student_id)
        serializer = StudentSerializer(student, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Student updated successfully'})
        return Response(serializer.errors, status=400)
    
    def delete(self,request,pk,format=None):
        student_id = pk
        student = Student.objects.get(id=student_id)
        student.delete()
        return Response({'msg': 'Student deleted successfully'}, status=204)
