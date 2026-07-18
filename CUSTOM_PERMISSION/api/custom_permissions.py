from rest_framework.permissions import BasePermission

class APIPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method=='GET':
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if obj.name==request.user:
            return True
        return False
