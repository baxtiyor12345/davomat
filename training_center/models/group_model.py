from django.db import models
from ..models import *
from .teacher_model import *

class Rooms(BaseModel):
    title=models.CharField(max_length=50)
    descriptions=models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

class TableType(BaseModel):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

class Table(BaseModel):
    start_time=models.TimeField()
    end_time=models.TimeField()
    room=models.ForeignKey(Rooms, on_delete=models.CASCADE)
    type=models.ForeignKey(TableType, on_delete=models.CASCADE)
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.start_time.__str__()+"  "+self.end_time.__str__()

class GroupStudent(BaseModel):
    title=models.CharField(max_length=200, unique=True)
    course=models.ForeignKey(Course, on_delete=models.CASCADE, related_name="groupcourse")
    teacher=models.ManyToManyField(Teacher, related_name="get_teacher")
    table=models.ForeignKey(Table, on_delete=models.CASCADE, related_name="group_tables")
    start_date=models.DateField()
    end_date=models.DateField()
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title








