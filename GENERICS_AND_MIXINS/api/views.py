from django.shortcuts import render
from rest_framework import generics,mixins
from .models import Student
from .serializers import StudentSerializer


# Create your views here.

class StudentListAPI(generics.GenericAPIView, mixins.ListModelMixin):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    # #Create
class StudentCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer 

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    #retrieve
class StudentRetrieveAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer  

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class StudentUpdateAPI(generics.GenericAPIView, mixins.UpdateModelMixin):   
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  
    #update(put)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    #update(patch)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class StudentDeleteAPI(generics.GenericAPIView, mixins.DestroyModelMixin):   
    queryset = Student.objects.all()
    serializer_class = StudentSerializer     
    #delete
    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)
     