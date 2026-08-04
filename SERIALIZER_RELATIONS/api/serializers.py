from rest_framework import serializers
from .models import Singer,Song

class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields='__all__'

class SingerSerializers(serializers.ModelSerializer):
    song=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    song=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-list')
    song=serializers.StringRelatedField(many=True,read_only=True)
    song=serializers.SlugRelatedField(many=True,read_only=True,slug_field='duration')
    class Meta:
        model=Singer
        fields=['id','name','gender','song']
