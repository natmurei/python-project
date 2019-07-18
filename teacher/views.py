from django.shortcuts import render
from .forms import TeacherForm
from .models import Teacher
from django.shortcuts import redirect

def add_teacher(request):
	if request.method=="POST":
		form=TeacherForm(request.POST)
		if form.is_valid():
			form.save()
		
	else:
		form = TeacherForm()
	return render(request,"add_teacher.html",{"form":form})

def list_teacher(request):
	teacher =Teacher.objects.all()
	return render(request,"list_teacher.html",{"teacher":teacher})
def teacher_detail(request,pk):
	teacher=Teacher.objects.get(pk=pk)
	return render(request,"teacher_detail.html",
		{"teacher":teacher})
def edit_teacher(request,pk):
	teacher=Teacher.objects.get(pk=pk)
	if request.method=="POST":
		form=TeacherForm(request.POST,instance=teacher)
		if form.is_valid:
			form.save()
	else:
		form=TeacherForm(instance=teacher)
	return render(request,"edit_teacher.html",{"form":form})


# Create your views here.
