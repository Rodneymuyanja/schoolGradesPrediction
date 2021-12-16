from django.db import models
from .apps import EndpointsConfig

# Create your models here.

class Grade(models.Model):
    grade = models.IntegerField()
    #mark = models.IntegerField()
    comment = models.CharField(max_length=250)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ["grade"] 

class Student(models.Model):
    regNo = models.CharField(max_length=50)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    classS = models.CharField(max_length=30)
    age = models.IntegerField()
    phoneNumber = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    residence = models.BooleanField()
    dateAdded = models.DateField()
    
    
    def __str__(self):
        return self.firstname

class Subject(models.Model):
    name = models.CharField(max_length=50) 
    compulsory = models.BooleanField() 

    def __str__(self):
        return self.name 

class Teacher(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    phoneNumber = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.ForeignKey(Subject, verbose_name="teacher", on_delete=models.CASCADE) 

    def __str__(self):
        return self.firstname

class Tests(models.Model):
    name = models.CharField(max_length=50)
    dateAdded = models.DateField()

    def __str__(self):
        return self.name


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    test = models.ForeignKey(Tests, on_delete=models.CASCADE, null=True)
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE, null=True)
    dateAdded = models.DateField()
    comment = models.CharField(max_length=50, null=True)
  
    def __str__(self):
        return self.comment
      


class Prediction(models.Model):
    """ student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    """
    student = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=50, null=True)
    prediction = models.IntegerField(null=True)
    dateGenerated = models.DateField()



    