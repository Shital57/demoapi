#create emoployee model
#Here we are providing relationship between model

from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=20)
    salary = models.FloatField()
    address = models.CharField(max_length=50)


    def __str__(self):
        return self.ename
