from django.contrib import admin

from . models import Faculty, Tribe, County



class FacultyAdmin(admin.ModelAdmin):
    model:Faculty
    list_display=('code','name')


admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Tribe)

class CountyAdmin(admin.ModelAdmin):
    model=County
    list_display=('code','name')
admin.site.register(County, CountyAdmin)