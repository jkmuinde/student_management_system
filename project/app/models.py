from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    user_type_data=(
        (1,'admin'),
        (2,'staff'),
        (3, 'student')
    )
    user_gender=(
        ('M','Male'),
        ('F', "Female")
    )
    user_type=models.CharField(default=None, choices=user_type_data,max_length=10,blank=False, null=False)
    gender=models.CharField(default=None, choices=user_gender, max_length=5, blank=False, null=False)


class AdminUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class StudentUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()




class Faculty(models.Model):
    code=models.CharField('Faculty Code', max_length=20, blank=False, null=False)
    name=models.CharField('Faculty', max_length=500, blank=False, null=False)

    class Meta:
        verbose_name='Faculty'
        verbose_name_plural='Falcuties'
        ordering='code',

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


@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in HOD, Staff or Student
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Staffs.objects.create(admin=instance)
        if instance.user_type == 3:
            Students.objects.create(admin=instance, course_id=Courses.objects.get(id=1), session_year_id=SessionYearModel.objects.get(id=1), address="", profile_pic="", gender="")
    

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.staffs.save()
    if instance.user_type == 3:
        instance.students.save()