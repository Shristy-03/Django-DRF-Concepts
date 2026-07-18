from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from .custom_permissions import APIPermission

# Create your views here.

class StudentAPI(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes=[APIPermission]
    
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentAPI_1(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
