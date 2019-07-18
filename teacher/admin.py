from django.contrib import admin
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
	list_display=("first_name","last_name","registration_number","email","date_joined")
admin.site.register(Teacher,TeacherAdmin)
# Register your models here.
