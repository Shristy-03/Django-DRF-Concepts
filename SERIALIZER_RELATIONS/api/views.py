from django.shortcuts import render
from .models import Singer,Song
from rest_framework import viewsets
from .serializers import SingerSerializers,SongSerializers

# Create your views here.

class SingerViewSet(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializers

class SongViewSet(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializers    