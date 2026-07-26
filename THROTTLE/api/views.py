from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,DjangoModelPermissions,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle
from .throttling import jackThrottle
# Create your views here.

class StudentAPI(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle,jackThrottle]
    
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentAPI_1(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='StudentAPI'
