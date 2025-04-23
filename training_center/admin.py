from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([Teacher, Student, Group, Departments, Parents, Rooms ,Table, TableType, GroupStudent])


