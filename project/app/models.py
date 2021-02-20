from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
# Create your models here.

YEAR_CHOICES = [(r,r) for r in range(1950, datetime.date.today().year-5)]

class Student(models.Model):
    regno=models.CharField('Registration Number',max_length=100, blank=False, null=False, )
    first_name=models.CharField("first name", blank=False, null=False, max_length=255)
    middle_name=models.CharField("first name", blank=False, null=False, max_length=255)
    surname=models.CharField("first name", blank=False, null=False, max_length=255)
    email=models.EmailField('Email Address', blank=True, null=True, max_length=255)
    phone=models.CharField('Phone Number', blank=True, null=True, max_length=255)

class StudentProfile(models.Model):
    student_type_data=(
        ('Part time','Part Time'),
        ('Rregular', "Regular"),
        ('GSSP','GSSP'),
        ('PSSP','PSSP')
    )
    accomodation_type=(
        ('Hostel','Hostels'),
        ('Rentals', "Rentals")
    )
    user_gender=(
        ('Male','Male'),
        ('Female', "Female")
    )
    student_type=models.CharField(default=None, choices=student_type_data,max_length=10,blank=False, null=False)
    accomodation=models.CharField(default=None, blank=True, null=True, choices=accomodation_type, max_length=10)
    gender=models.CharField(default=None, choices=user_gender, max_length=100, blank=False, null=False)
    course=models.ForeignKey('Course', help_text='COurse taken', on_delete=models.CASCADE, null=True, blank=True)
    tribe=models.ForeignKey('Tribe', on_delete=models.SET_NULL, blank=True, null=True)
    county=models.ForeignKey('County', on_delete=models.SET_NULL, blank=True, null=True)
    profile = models.OneToOneField(Student, on_delete=models.CASCADE)
    yob=models.IntegerField("Year of Birth", choices=YEAR_CHOICES, default=datetime.datetime.now().year-15)

    def __str__(self):  # __unicode__ for Python 2
        return self.profile.first_name + " "+self.profile.first_name+" "+self.profile.first_name





class Faculty(models.Model):
    code=models.CharField('Faculty Code', max_length=20, blank=False, null=False)
    name=models.CharField('Faculty', max_length=500, blank=False, null=False)

    class Meta:
        verbose_name='Faculty'
        verbose_name_plural='Falcuties'
        ordering='code',

    def __str__(self):
        return self.code

class Course(models.Model):
    code=models.CharField('Course Code', blank=False, null=False, max_length=100)
    name=models.CharField('Course taken', blank=False, null=False, max_length=255)
    faculty=models.ForeignKey(Faculty, on_delete=models.CASCADE)

    class Meta:
        ordering='code',
        verbose_name_plural='Courses'

    def __str__(self):
        return self.code


class Tribe(models.Model):
    name=models.CharField('Ethnic Group', blank=False, null=False, max_length=255)

    class Meta:
        ordering='name',

    def __str__(self):
        return self.name.capitalize() + " Tribe(s)"

class County(models.Model):
    code=models.IntegerField('County Code', blank=False, null= False, max_length=2, unique=True)
    name=models.CharField("County Name", max_length=100, blank=False, null=False)


    class Meta:
        verbose_name='County'
        verbose_name_plural='Counties'
        ordering='code',

    def __str__(self):
        f_name=self.name
        return f_name.capitalize() + " County"
