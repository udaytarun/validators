from django.db import models

# Create your models here.

class Student(models.Model):
    Sname=models.CharField(max_length=100)
    Sage=models.IntegerField()
    Sid=models.IntegerField()
    Semail=models.EmailField()
    mobile=models.CharField(max_length=10)

    def __str__(self):
        return self.Sname
