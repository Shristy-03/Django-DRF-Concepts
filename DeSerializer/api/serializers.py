from rest_framework import serializers
from .models import Student

#validators 
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError("Name should be start with R")

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        print(instance.roll)
        instance.city = validated_data.get('city', instance.city)
        print(instance.city)
        instance.save()
        return instance

    #field_level_validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value
    
    # object_level_validation
    def validate(self, data):
        print("Object validation called")
        nm = data.get('name')
        ct = data.get('city')

        if nm.lower() == 'shyam' and ct.lower() != 'ludhiana':
            raise serializers.ValidationError(
                "City must be Ludhiana for Shyam"
            )
        return data

