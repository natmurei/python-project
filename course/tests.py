from django.test import TestCase
import datetime
from.forms import CourseForm
from django.urls import reverse
from django.test import Client
client = Client()

# Create your tests here.

class CreateCourseTestCase(TestCase):
	def setUp(self):
		self.data={"Name" : "Natasha",
	               "Duration_in_months" : "9",
	               "course_number" : "222",
	               "Description" : "python subject",
	              
				   }

		self.bad_data={"Name" : 666666,
	               "Duration_in_months" : "9 months",
	               "course_number" : "222",
	               "Description" : "python subject",
	               "teachers" :"mwai",
				   }

	def test_course_form_accepts_valid_data(self):
		form=CourseForm(self.data)
		self.assertTrue(form.is_valid())

	def test_course_form_rejects_invalid_data(self):
		form=CourseForm(self.bad_data)
		self.assertFalse(form.is_valid())

	def test_add_course_view(self):
		url=reverse("add_student")
		request=client.post(url, self.data)
		self.assertEqual(request.status_code,200)

	def test_add_course_view_bad_data(self):
		url=reverse("add_student")
		request=client.post(url, self.bad_data)
		self.assertEqual(request.status_code,400)
