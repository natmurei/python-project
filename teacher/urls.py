from django.urls import path
from .views import add_teacher,list_teacher

urlpatterns=[
path("add/",add_teacher,name="add_teacher"),
path("list/",list_teacher,name="list_teacher")
]
