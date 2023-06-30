import re
from django.db import models

# Create your models here.
class studnet(models.Model):
    studentname = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    student_id=models.CharField(max_length=50)
    gpa=models.DecimalField(max_digits=3,decimal_places=2)
    level=models.CharField(max_length=1)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    activation=models.CharField(max_length=10)



   
    def __str__(self):
        return self.student_id



    class Meta:
        verbose_name='FCAI_students'

    class Meta:
        ordering = ['student_id']
