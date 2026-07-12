from rest_framework import serializers
from .models import Student

# model serializers 
class StudentSerializer(serializers.ModelSerializer):
    # custom field level validation
    def name_length(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Name is too short")
        return value
    name=serializers.CharField(max_length=100, validators=[name_length])
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        
        # field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value  
    
    # object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'aaryadha' and ct.lower() != 'delhi':
            raise serializers.ValidationError("City must be Delhi")
        return data   




    

    

