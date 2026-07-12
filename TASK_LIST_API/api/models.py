from django.db import models

# Create your models here.
class Task(models.Model):
    status_choices = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=status_choices, default='pending')

    def __str__(self):
        return self.title