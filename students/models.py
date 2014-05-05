from django.db import models
from classes.models import Class

# Create your models here.
class Student(models.Model):
    student_id=models.IntegerField(primary_key=True)
    first_name=models.TextField()
    last_name=models.TextField()
    gender=models.CharField(max_length=10)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)    
    classid=models.ForeignKey(Class)
    
    
    def _unicode_(self):
        self.student_id
        