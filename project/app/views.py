from django.db import models
from django.shortcuts import render
from django.views import generic
from . models import Faculty, County, Tribe, Course, Student

# Create your views here.
def index(request):
    all_student_count = Student.objects.all().count()
    all_faculty_count = Faculty.objects.all().count()
    all_county_count = County.objects.all().count()
    all_tribe_count= Tribe.objects.all().count()
    all_course_count=  Course.objects.all().count()


    context={}
    template_name='admin/home.html'
    return render(request, template_name, context)

class StudentList(generic.ListView):
    model=Student
    tenplate_name='app/student_list.html'

class StudentDetail(generic.DetailView):
    model=Student
    template_name='app/student_detail.html'

class FacultyList(generic.ListView):
    model=Faculty
    tenplate_name='app/faculty_list.html'

class FacultyDetail(generic.DetailView):
    model=Faculty
    template_name='app/faculty_detail.html'

class CourseList(generic.ListView):
    model=Course
    tenplate_name='app/course_list.html'

class CourseDetail(generic.DetailView):
    model=Course
    template_name='app/course_detail.html'

class CountyList(generic.ListView):
    model=County
    tenplate_name='app/county_list.html'

class CountyDetail(generic.DetailView):
    model=County
    template_name='app/county_detail.html'

class TribeList(generic.ListView):
    model=Tribe
    template_name='adappmin/tribe_list.html'

class TribeDetail(generic.DetailView):
    model=Tribe
    template_name='app/tribe_detail.html'