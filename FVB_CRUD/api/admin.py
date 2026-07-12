from django.contrib import admin
from.models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll_number', 'city')
    search_fields = ('name', 'roll_number', 'city')
    list_filter = ('city',) 
