# from django.db import models
# from ..models import *
#
# class Davomat(models.Model):
#     group=models.ForeignKey('training_center.GroupStudent', on_delete=models.CASCADE)
#     date=models.DateField()
#     descriptions=models.TextField(blank=True)
#
#     def __str__(self):
#         return f"{self.group}-{self.date}"
#
#
# class StudentDavomati(models.Model):
#     STATUS_CHOICES=[
#         ("bor","Bor"),
#         ("yo`q", "Yo`q"),
#         ("kechikkan", "Kechikkan"),
#         ("sababli", "Sababli")
#     ]
#
#     davomat=models.ForeignKey(Davomat,on_delete=models.CASCADE, related_name="student_davomati")
#     student=models.ForeignKey('training_center.Student', on_delete=models.CASCADE)
#     status=models.CharField(max_length=10, choices=STATUS_CHOICES)
#
#
#
#
#
# class TeacherDavomati(models.Model):
#     STATUS_CHOICES=[
#         ("bor","Bor"),
#         ("yo`q", "Yo`q"),
#         ("kechikkan", "Kechikkan"),
#         ("sababli", "Sababli")
#     ]
#
#     davomat=models.ForeignKey(Davomat,on_delete=models.CASCADE, related_name="teacher_davomati")
#     teacher=models.ForeignKey('training_center.Teacher', on_delete=models.CASCADE)
#     status=models.CharField(max_length=10, choices=STATUS_CHOICES)

#
# from django.db import models
# from .student_model import Group, Student
# class Groups(models.Model):
#     name = models.CharField(max_length=100)
#     created_at = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#
# class Students(models.Model):
#     full_name = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=20)
#     enrolled_date = models.DateField(auto_now_add=True)
#     group = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name='students')
#
#     def __str__(self):
#         return self.full_name
#
# class Attendance(models.Model):
#     student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='attendances')
#     date = models.DateField()
#     status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])
#
#     def __str__(self):
#         return f"{self.student.full_name} - {self.date} - {self.status}"


from django.db import models

class Groups(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student_name = models.CharField(max_length=100)
    group = models.ForeignKey(Groups, related_name="attendances", on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=False)  # True - present, False - absent

    def __str__(self):
        return f"{self.student_name} - {self.status} on {self.date}"
