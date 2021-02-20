from django.db import models
from django.db.models import Count
from django.shortcuts import render
from django.views import generic
from . models import Faculty, County, StudentProfile, Tribe, Course, Student

# Create your views here.
def index(request):

    #count objects in all models
    student_count=Student.objects.all().count()
    faculty_count=Faculty.objects.all().count()
    course_count=Course.objects.all().count()
    tribe_count=Tribe.objects.all().count()
    county_count=County.objects.all().count()

    #student per course
    course_all=Course.objects.all()
    course_name_list=[]
    student_count_list_per_course=[]

    for course in course_all:
        students=StudentProfile.objects.filter(course=course.id).count()
        course_name_list.append(course.name)
        student_count_list_per_course.append(students)

    #course per faculty
    faculty_all=Faculty.objects.all()
    faculty_name_list=[]
    course_list_count_per_faculty=[]

    for faculty in faculty_all:
        courses=Course.objects.filter(faculty=faculty.id).count()
        faculty_name_list.append(faculty)
        course_list_count_per_faculty.append(courses)


    #student count per tribe
    tribe_all=Tribe.objects.all()
    tribe_name_list=[]
    student_list_count_per_tribe=[]

    for tribe in tribe_all:
        students=StudentProfile.objects.filter(tribe=tribe.id).count()
        tribe_name_list.append(tribe)
        student_list_count_per_tribe.append(students)

    #student count per county
    county_all=County.objects.all()
    county_name_list=[]
    student_count_list_per_county=[]

    for county in county_all:
        students=StudentProfile.objects.filter(county=county.id).count()
        county_name_list.append(county)
        student_count_list_per_county.append(students)



        
    context={
        'student_count':student_count,
        'faculty_count':faculty_count,
        'course_count':course_count,
        'tribe_count':tribe_count,
        'county_count':county_count,

        #student per course
        'course_name_list':course_name_list,
        'student_count_list_per_course':student_count_list_per_course,


        #course count per faculty
        'faculty_name_list':faculty_name_list,
        'course_list_count_per_faculty':course_list_count_per_faculty,


        #student count per tribe
        'tribe_name_list':tribe_name_list,
        'student_list_count_per_tribe':student_list_count_per_tribe,



        #student count per county
        'county_name_list':county_name_list,
        'student_count_list_per_county':student_count_list_per_county
    }
    template_name='admin/home.html'
    return render(request, template_name, context)

class StudentProfileList(generic.ListView):
    model=StudentProfile
    tenplate_name='app/student_list.html'

class StudentProfileDetail(generic.DetailView):
    model=StudentProfile
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