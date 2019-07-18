from django.urls import path
from .views import add_student, list_student, student_detail,edit_student


urlpatterns=[
path("add/",add_student,name="add_student"),
path("list/",list_student,name="list_student"),
path("detail/<int:pk>/",student_detail,name="student_detail"),
path("edit/<int:pk>/",student_detail,name="student_edit"),
]