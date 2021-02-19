from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('falcuties/', views.FacultyList.as_view(), name='faculties'),
    path('falcuties/<int:pk>/', views.FacultyDetail.as_view(), name='faculty_detail'),
    path('counties/', views.CountyList.as_view(), name='counties'),
    path('counties/<int:pk>/', views.CountyDetail.as_view(), name='county_detail'),
    path('courses/', views.CourseList.as_view(), name='courses'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='course_detail'),
    path('tribes/', views.TribeList.as_view(), name='tribes'),
    path('tribes/<int:pk>/', views.TribeDetail.as_view(), name='triibe_detail'),
    path('students/', views.StudentList.as_view(), name='students'),
    path('students/<int:pk>/', views.StudentDetail.as_view(), name='student_detail'),
]
