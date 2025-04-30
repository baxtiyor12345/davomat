# from rest_framework import serializers
# from training_center.models import *
#
# class StudentDavomatSerializer(serializers.ModelSerializer):
#     student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
#
#     class Meta:
#         model = StudentDavomati
#         fields = ['student', 'status']
#
# class DavomatCreateSerializer(serializers.Serializer):
#     group = serializers.PrimaryKeyRelatedField(queryset=GroupStudent.objects.all())
#     date = serializers.DateField()
#     descriptions = serializers.CharField(required=False, allow_blank=True)
#     davomat = serializers.DictField(
#         child=serializers.ChoiceField(choices=["bor", "yo'q", "kechikkan","sababli"])
#     )
#
#     def create(self, validated_data):
#         group = validated_data['group']
#         date = validated_data['date']
#         descriptions = validated_data.get('descriptions', '')
#         davomat = Davomat.objects.create(group=group, date=date, descriptions=descriptions)
#
#         student_davomat = []
#         for student_id_str, status in validated_data['davomat'].items():
#             student_id = int(student_id_str)
#             student = Student.objects.get(pk=student_id)
#             student_davomat.append(
#                 StudentDavomati(davomat=davomat, student=student, status=status)
#             )
#
#         StudentDavomati.objects.bulk_create(student_davomat)
#         return davomat
#
# class TeacherDavomatSerializer(serializers.ModelSerializer):
#     teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
#
#     class Meta:
#         model = TeacherDavomati
#         fields = ['teacher', 'status']
#
# class TeacherCreateSerializer(serializers.Serializer):
#     group = serializers.PrimaryKeyRelatedField(queryset=GroupStudent.objects.all())
#     date = serializers.DateField()
#     descriptions = serializers.CharField(required=False, allow_blank=True)
#     davomat = serializers.DictField(
#         child=serializers.ChoiceField(choices=["bor", "yo'q", "kechikkan","sababli"])
#     )
#
#     def create(self, validated_data):
#         group = validated_data['group']
#         date = validated_data['date']
#         descriptions = validated_data.get('descriptions', '')
#         davomat = Davomat.objects.create(group=group, date=date, descriptions=descriptions)
#
#         teacher_davomat = []
#         for teacher_id_str, status in validated_data['davomat'].items():
#             teacher_id = int(teacher_id_str)
#             teacher = Teacher.objects.get(pk=teacher_id)
#             teacher_davomat.append(
#                 TeacherDavomati(davomat=davomat, teacher=teacher, status=status)
#             )
#         TeacherDavomati.objects.bulk_create(teacher_davomat)
#         return davomat


# from rest_framework import serializers
# from ..models import Groups, Students, Attendance
#
# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Groups
#         fields = '__all__'
#
# class StudentSerializer(serializers.ModelSerializer):
#     group_name = serializers.CharField(source='group.name', read_only=True)
#
#     class Meta:
#         model = Students
#         fields = ['id', 'full_name', 'phone_number', 'enrolled_date', 'group', 'group_name']
#
# class AttendanceSerializer(serializers.ModelSerializer):
#     student_name = serializers.CharField(source='student.full_name', read_only=True)
#
#     class Meta:
#         model = Attendance
#         fields = ['id', 'student', 'student_name', 'date', 'status']

from rest_framework import serializers
from ..models import Attendance, Groups

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'student_name', 'group', 'date', 'status']

class GroupSerializer(serializers.ModelSerializer):
    attendances = AttendanceSerializer(many=True, read_only=True)

    class Meta:
        model = Groups
        fields = ['id', 'name', 'description', 'attendances']
