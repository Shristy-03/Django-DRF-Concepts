from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll_no', 'city']
    list_filter = ['city']
    search_fields = ['name', 'roll_no']