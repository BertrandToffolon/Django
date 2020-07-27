from django.contrib import admin
# Register your models here.
from .models import Student
from .models import Cursus
from .models import Presence

class StudentAdmin(admin.ModelAdmin):
    list_display= ("first_name", "last_name","email","phone")
class CursusAdmin(admin.ModelAdmin):
    list_display= ("scholar_year", "name","year_from_bac") 
class PresenceAdmin(admin.ModelAdmin):
    list_display= ("reason","isMissing","date","start_time","stop_time")

admin.site.register(Student,StudentAdmin)
admin.site.register(Cursus,CursusAdmin)
admin.site.register(Presence,PresenceAdmin)
