from django.db import models
from teacher.models import Teacher
class Course(models.Model):
	Name=models.CharField(max_length=50)
	Duration_in_months=models.SmallIntegerField()
	course_number=models.CharField(max_length=50)
	Description=models.TextField(max_length=50)
	teachers=models.ForeignKey(Teacher,on_delete=models.PROTECT)
	def __str__(self):
		return self.Name
# Create your models here.
