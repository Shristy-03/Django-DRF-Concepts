from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

class student_list(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class student_create(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class student_retrieve(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class student_update(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class student_del(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class student_list_create(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class student_retrieve_update(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class student_retrieve_destroy(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer    

class student_retrieve_update_destroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer    



