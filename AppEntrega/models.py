from django.db import models

# Create your models here.

class empleado(models.Model):
    id=models.IntegerField
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

class cliente(models.Model):
    id=models.IntegerField
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

class proveedor(models.Model):
    id=models.IntegerField
    nombre=models.CharField(max_length=50)
    apellido=models.IntegerField
    email=models.EmailField()


