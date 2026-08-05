from django.shortcuts import render
from .models import Singer
from rest_framework import viewsets
from .serializers import SingerSerializer
# Create your views here.

class SingerViewSet(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer

