from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db.models import deletion
from . models import Faculty, Tribe, County, Course , Student, StudentProfile

class CourseAdmin(admin.ModelAdmin):
    model=Course
    list_display=('code','name')

admin.site.register(Course,CourseAdmin)

class CourseInline(admin.StackedInline):
    model = Course
    can_delete = False

class FacultyAdmin(admin.ModelAdmin):
    model=Faculty
    inlines=CourseInline,
    list_display=('code','name')


admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Tribe)

class CountyAdmin(admin.ModelAdmin):
    model=County
    list_display=('code','name')
admin.site.register(County, CountyAdmin)


class StudentProfileInline(admin.TabularInline):
    model=StudentProfile
    deletion=False



class StudentAdmin(admin.ModelAdmin):
    model=Student
    list_display=('first_name','middle_name','surname')
    inlines=StudentProfileInline,


admin.site.register(Student, StudentAdmin)
