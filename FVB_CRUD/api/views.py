from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request, student_id=None):
    if request.method == 'GET':
        id=student_id
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
        
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Student created successfully'}, status=201)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'PUT':
        student_id = student_id
        student = Student.objects.get(id=student_id)
        serializer = StudentSerializer(student, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Student updated successfully'})
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        student_id = student_id
        student = Student.objects.get(id=student_id)
        student.delete()
        return Response({'msg': 'Student deleted successfully'}, status=204)  
    return Response(serializer.errors, status=405)  
        