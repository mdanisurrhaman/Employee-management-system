from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()


class Department(models.Model):
    name=models.CharField(max_length=200)
    hod=models.CharField(max_length=100)




class Student(models.Model):
    name=models.CharField(max_length=20)
    roll_no=models.IntegerField()
    semester=models.IntegerField()
    # branch=models.CharField(max_length=10)
    phone_no=models.IntegerField()  


class contactenquiry(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    massege=models.CharField(max_length=200)      
