from django.db import models

# Create your models here.
class MyData(models.Model):
    myid=models.CharField(max_length=1000)
    description=models.CharField(max_length=50)


# def __str__(self):
#         return self.id