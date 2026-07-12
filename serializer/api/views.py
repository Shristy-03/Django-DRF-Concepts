from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

## model object-single student data

def student_detail(request):
    stu=Student.objects.get(id=1)
    print(stu)
    print(type(stu))

    serializer=StudentSerializer(stu)
    print(serializer.data)
    print(type(serializer.data))

    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

def student_detail_pk(request, pk):
    stu=Student.objects.get(id=pk)
    print(stu)
    print(type(stu))

    serializer=StudentSerializer(stu)
    print(serializer.data)
    print(type(serializer.data))
    
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

## QuerySet - multiple student data

def student_list(request):
    students = Student.objects.all()
    print(students)

    serializer = StudentSerializer(students, many=True)
    print(serializer.data)

    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)
