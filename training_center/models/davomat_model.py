from django.db import models
from ..models import *

class Davomat(models.Model):
    group=models.ForeignKey('training_center.GroupStudent', on_delete=models.CASCADE)
    date=models.DateField()
    descriptions=models.TextField(blank=True)

    def __str__(self):
        return f"{self.group}-{self.date}"


class StudentDavomati(models.Model):
    STATUS_CHOICES=[
        ("bor","Bor"),
        ("yo`q", "Yo`q"),
        ("kechikkan", "Kechikkan"),
        ("sababli", "Sababli")
    ]

    davomat=models.ForeignKey(Davomat,on_delete=models.CASCADE, related_name="student_davomati")
    student=models.ForeignKey('training_center.Student', on_delete=models.CASCADE)
    status=models.CharField(max_length=10, choices=STATUS_CHOICES)





class TeacherDavomati(models.Model):
    STATUS_CHOICES=[
        ("bor","Bor"),
        ("yo`q", "Yo`q"),
        ("kechikkan", "Kechikkan"),
        ("sababli", "Sababli")
    ]

    davomat=models.ForeignKey(Davomat,on_delete=models.CASCADE, related_name="teacher_davomati")
    teacher=models.ForeignKey('training_center.Teacher', on_delete=models.CASCADE)
    status=models.CharField(max_length=10, choices=STATUS_CHOICES)