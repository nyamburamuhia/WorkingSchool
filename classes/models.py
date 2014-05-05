from django.db import models

# Create your models here.

class Class(models.Model):
    class_id=models.IntegerField(primary_key=True)
    class_name=models.CharField(max_length=100)
    
    def _unicode_(self):
        self.class_id
