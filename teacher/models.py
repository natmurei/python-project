from django.db import models
class Teacher(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	id_number=models.IntegerField()
	email=models.EmailField(max_length=50)
	phone_number=models.CharField(max_length=50)
	registration_number=models.CharField(max_length=50)
	date_joined=models.DateField()
	

	def __str__(self):
		return self.first_name+" "+self.last_name
# Create your models here.
