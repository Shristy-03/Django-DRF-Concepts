from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .custom_auth import custom_auth

from rest_framework.permissions import AllowAny,IsAuthenticated,DjangoModelPermissions,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions

# Create your views here.

class StudentAPI(viewsets.ModelViewSet):
    authentication_classes=[custom_auth]
    # # permission_classes=[AllowAny]
    permission_classes=[IsAuthenticated]
    # # permission_classes=[IsAuthenticatedOrReadOnly]
    # # permission_classes=[IsAdminUser]
    # # permission_classes=[DjangoModelPermissions]
    # # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes=[DjangoObjectPermissions]
    
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentAPI_1(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
