# from rest_framework.views import APIView
# from rest_framework.response import Response
# from drf_yasg.utils import swagger_auto_schema
# from ..serializers import *
# from training_center.models import Teacher
# from training_center.serializers import *
#
# class StudentDavomatiApi(APIView):
#     @swagger_auto_schema(request_body=DavomatCreateSerializer)
#     def post(self, request):
#         serializer = DavomatCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         davomat = serializer.save()
#         data = {
#             "success": True,
#             "data": {
#                 "id": davomat.id,
#                 "date": davomat.date,
#                 "group": davomat.group.id,
#                 "descriptions": davomat.descriptions
#             }
#         }
#         return Response(data=data, status=201)
#
#     def get(self, request):
#         student_davomat = StudentDavomati.objects.all().order_by('-id')
#         serializer = StudentDavomatSerializer(student_davomat, many=True)
#         return Response(data=serializer.data)
#
#
#
# class TeacherDavomatiApi(APIView):
#     @swagger_auto_schema(request_body=TeacherCreateSerializer)
#     def post(self, request):
#         serializer = TeacherCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         davomat = serializer.save()
#         data = {
#             "success": True,
#             "data": {
#                 "id": davomat.id,
#                 "date": davomat.date,
#                 "group": davomat.group.id,
#                 "descriptions": davomat.descriptions
#             }
#         }
#         return Response(data=data, status=201)
#
#     def get(self, request):
#         teacher_davomat = TeacherDavomati.objects.all().order_by('-id')
#         serializer = TeacherDavomatSerializer(teacher_davomat, many=True)
#         return Response(data=serializer.data)


# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework import status, viewsets
# from ..models import Groups, Students, Attendance
# from ..serializers import GroupSerializer, StudentSerializer, AttendanceSerializer
# from datetime import date
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Groups.objects.all()
#     serializer_class = GroupSerializer
#
#     @action(detail=True, methods=['post'])
#     def mark_attendance(self, request, pk=None):
#         group = self.get_object()
#         students = group.students.all()
#         attendance_date = request.data.get('date', date.today())
#         present_ids = request.data.get('present_ids', [])  # borlar id si ro'yxati
#
#         if not isinstance(present_ids, list):
#             return Response({"error": "present_ids list bo'lishi kerak"}, status=status.HTTP_400_BAD_REQUEST)
#
#         created_records = []
#         for student in students:
#             status_ = 'Present' if student.id in present_ids else 'Absent'
#             obj, created = Attendance.objects.get_or_create(
#                 student=student,
#                 date=attendance_date,
#                 defaults={'status': status_}
#             )
#             if not created:
#                 # oldingi attendance bo'lsa ham statusini update qilamiz
#                 obj.status = status_
#                 obj.save()
#             created_records.append(obj)
#
#         return Response({
#             "message": f"{len(created_records)} ta attendance yozildi yoki yangilandi.",
#         }, status=status.HTTP_201_CREATED)

from rest_framework import viewsets
from ..models import Groups, Attendance
from ..serializers import GroupSerializer, AttendanceSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer

    @action(detail=True, methods=['get'])
    def attendances(self, request, pk=None):
        group = self.get_object()
        attendances = Attendance.objects.filter(group=group)
        serializer = AttendanceSerializer(attendances, many=True)
        return Response(serializer.data)

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
