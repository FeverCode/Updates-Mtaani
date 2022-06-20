from re import I
from django.contrib import admin
from .models import *

# Register your models here.
class NeighbourhoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'admin','occupants', 'description', 'hospital_tel', 'police_tel')



admin.site.register(Neighbourhood, NeighbourhoodAdmin)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Post)
