from django.test import TestCase

from.models import Teacher
import datetime
from.forms import TeacherForm
from django.urls import reverse
from django.test import Client
client=Client()

class CreateTeacherTestCase(TestCase):
    def setUp(self):
        self.data={"first_name" : "James",
				   "last_name" : "Mwai",
				   "email" :"jamesmwai@AkiraChix.com",
				   "phone_number" :"0724228420",
				   "id_number" :44446345,
				   "date_joined" :datetime.date.today(),
				   }
		self.bad_data={"first_name" : "James",
				   "last_name" : "Mwai",
				   "email" :"jamesmwai@AkiraChix.com",
				   "phone_number" :"0724228420",
				   "id_number" :"44446345",
				   "date_joined" :datetime.date.today(),
				   }

    # def test_teacher_form_accepts_valid_data(self):
    #     form = TeacherForm(self.data)
    #     self.assertTrue(form.is_valid())
    # def test_teacher_form_rejects_invalid_data(self):
    #     form = TeacherForm(self.bad_data)
    #     self.assertFalse(form.is_valid())
    # def test_add_teacher_view(self):
    #     url=reverse("add_teacher")
    #     request=client.post(url, self.data)
    #     self.assertEqual(request.status_code,200)
    # def test_accept_add_teacher_view(self):
    #     url=reverse("add_teacher")
    #     request=client.post(url, self.bad_data)
    #     self.assertEqual(request.status_code,400)