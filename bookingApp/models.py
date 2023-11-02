from django.db import models

# Create your models here.
class categories(models.Model):
     categoryName=models.CharField(max_length=50)
     
     def __str__(self) :
        return f"{self.id}   {self.categoryName}"



class Course(models.Model):
    coursesName=models.CharField(max_length=50)
    Description=models.TextField(max_length=50)
    image=models.CharField(max_length=100)
    
    is_puplish=models.BooleanField()
    cateoryID=models.ForeignKey(categories,on_delete=models.CASCADE)
    
    def __str__(self) :
        return f"{self.id}   {self.coursesName}"



class Booking(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    email=models.EmailField(max_length=250)
    phone=models.IntegerField()
    age=models.IntegerField()
    coursesID=models.ForeignKey(Course,on_delete=models.CASCADE)
    
    