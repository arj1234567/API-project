from django.db import models
class Employe_tb(models.Model):
    Name=models.CharField(max_length=20)
    Age = models.IntegerField()
    City = models.CharField(max_length=20)
    Salary = models.PositiveIntegerField()
    
    
        

# Create your models here.
