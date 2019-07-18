from django.shortcuts import render
from .forms import CourseForm
from .models import Course
from django.shortcuts import redirect

def add_course(request):
	if request.method=="POST":
		form=CourseForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect("list_course")
	else:
	    form=CourseForm()
	return render(request,"add_course.html",{"form":form})
def list_course(request):
	course =Course.objects.all()
	return render(request,"list_course.html",{"course":course})

def course_detail(request,pk):
	course=Course.objects.get(pk=pk)
	return render(request,"course_detail.html",
		{"course":course})

def edit_course(request,pk):
	course=Course.objects.get(pk=pk)
	if request.method=="POST":
		form=CourseForm(request.POST,instance=course)
		if form.is_valid:
			form.save()
	else:
		form=CourseForm(instance=course)
	return render(request,"edit_course.html",{"form":form})


# Create your views here.
