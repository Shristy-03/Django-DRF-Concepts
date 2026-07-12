from rest_framework import serializers
from .models import Task
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  

    def validate_due_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value
    
    def validate_status(self, value):
        if value not in dict(Task.status_choices).keys():
            raise serializers.ValidationError("Invalid status choice.")
        return value
    
    def validate(self, data):
        if data['status'] == 'completed' and data['due_date'] > timezone.now().date():
            raise serializers.ValidationError("A task cannot be marked as completed if its due date is in the future.")
        if data['title'] == '':
            raise serializers.ValidationError("Title cannot be empty.")     
        if data['description'] == '':
            raise serializers.ValidationError("Description cannot be empty.")
        if len(data['title']) < 10:
            raise serializers.ValidationError("Title must be at least 10 characters long.")
        return data     