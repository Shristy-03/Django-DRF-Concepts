from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
    list_filter = ['city']
    search_fields = ['name', 'roll', 'city']


# Register your models here.
