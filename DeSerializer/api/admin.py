from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city')
    search_fields = ('name', 'roll', 'city')
    list_filter = ('name',)

# Register your models here.
