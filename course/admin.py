from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
	list_display=("Name","Duration_in_months","course_number","Description")
	search_fields=("teachers__last_name","course_number","Description")
	list_filter=("teachers__first_name","teachers__email",)
admin.site.register(Course,CourseAdmin)
# Register your models here.
# Register your models here.
