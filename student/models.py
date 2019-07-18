from django.db import models
from course.models import Course

class Student(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	date_of_birth=models.DateField()
	registration_number=models.CharField(max_length=50)
	place_of_residence=models.CharField(max_length=50)
	phone_number=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	guardian_phone=models.EmailField(max_length=50)
	id_number=models.IntegerField()
	date_joined=models.DateField()
	course=models.ManyToManyField(Course)
	

	def __str__(self):
		return self.first_name+" "+self.last_name 

# Create your models here.
