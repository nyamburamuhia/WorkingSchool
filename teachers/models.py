from django.db import models
from classes.models import Class

# Create your models here.
class Teacher(models.Model):
    teacher_id=models.IntegerField(primary_key=True)
    first_name=models.TextField()
    last_name=models.TextField()
    gender=models.CharField(max_length=10)
    classid=models.ForeignKey(Class)
      
    def _unicode_(self):
        self.teacher_id
