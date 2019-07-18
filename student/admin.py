from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display=("first_name","last_name","registration_number","email","date_joined")
	search_fields=("registration_number","last_name","email")
	list_filter=("email","date_joined")

admin.site.register(Student,StudentAdmin)

# Register your models here.
