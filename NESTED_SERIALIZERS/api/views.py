from django.shortcuts import render
from .models import Singer,Song
from rest_framework import viewsets
from .serializers import SingerSerializer,SongSerializer

# Create your views here.

class SingerViewSet(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer    