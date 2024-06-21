from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=32)
    rollno=models.IntegerField()
    marks=models.FloatField()


# Create your models here.
