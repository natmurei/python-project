from django.urls import path
from .views import add_course,list_course,course_detail,edit_course

urlpatterns=[
path("add/",add_course,name="add_course"),
path("list/",list_course,name="list_course"),
path("detail/<int:pk>/",course_detail,name="course_detail"),
path("edit/<int:pk>/",edit_course,name="edit_course"),
]