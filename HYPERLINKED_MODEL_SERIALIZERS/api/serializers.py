from rest_framework import serializers
from .models import Singer

class SingerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Singer
        fields=['id','url','name','gender']