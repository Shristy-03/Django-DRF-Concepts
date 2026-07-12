from django.shortcuts import render
from.models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
#get
def task_api(request, task_id=None):
    if request.method == 'GET':
        id = task_id
        if id is not None:
            if id not in Task.objects.values_list('id', flat=True):
                return Response({'msg': 'Resource not found'}, status=404)
            
            task = Task.objects.get(id=id)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        
        elif id is None:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        else:
            return Response({'msg': 'Resource not found'}, status=404)
    
    #post
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Task created successfully'}, status=201)
        return Response(serializer.errors, status=400)
    
    #put
    elif request.method == 'PUT':
        task_id = task_id
        if task_id not in Task.objects.values_list('id', flat=True):
            return Response({'msg': 'Resource not found'}, status=404)
        
        task = Task.objects.get(id=task_id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Task updated successfully'})
        return Response(serializer.errors, status=400)
    
    #patch
    elif request.method == 'PATCH':
        task_id = task_id
        if task_id not in Task.objects.values_list('id', flat=True):
            return Response({'msg': 'Resource not found'}, status=404)
        
        task = Task.objects.get(id=task_id)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Task partially updated successfully'})
        return Response(serializer.errors, status=400)
    
    #delete
    elif request.method == 'DELETE':
        task_id = task_id
        if task_id not in Task.objects.values_list('id', flat=True):
            return Response({'msg': 'Resource not found'}, status=404)
        
        task = Task.objects.get(id=task_id)
        task.delete()
        return Response({'msg': 'Task deleted successfully'}, status=204)

