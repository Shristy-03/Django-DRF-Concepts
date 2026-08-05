from django.contrib import admin
from .models import Singer
# Register your models here.

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display=['id','name','gender']


