from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([Teacher, Student, Groups, Group, Attendance, Departments, Parents, Rooms ,Table, TableType, GroupStudent])


