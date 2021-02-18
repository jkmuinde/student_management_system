from django.db import models

# Create your models here.

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
        return self.name + " Tribe(s)"

class County(models.Model):
    code=models.IntegerField('County Code', blank=False, null= False, max_length=2)
    name=models.CharField("County Name", max_length=100, blank=False, null=False)


    class Meta:
        verbose_name='County'
        verbose_name_plural='Counties'
        ordering='code',

    def __str__(self):
        return "0"+self.code + " " + self.name + " County"


