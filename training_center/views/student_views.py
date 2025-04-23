from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import *
from training_center.models import Student
from training_center.serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from ..models import Student, Group
from ..serializers import StudentSerializer
#
# class AssignStudentToGroup(APIView):
#     permission_classes = [IsAdminUser]  # Faqat adminlarga ruxsat
#
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 student = Student.objects.get(id=serializer.validated_data['student_id'])
#                 group = Group.objects.get(id=serializer.validated_data['group_id'])
#                 student.group = group
#                 student.save()
#                 return Response({"message": "Talaba groupga muvaffaqiyatli qo‘shildi."}, status=200)
#             except Student.DoesNotExist:
#                 return Response({"error": "Bunday student topilmadi"}, status=404)
#             except Group.DoesNotExist:
#                 return Response({"error": "Bunday group topilmadi"}, status=404)
#         return Response(serializer.errors, status=400)
#
#
#
# class UserStudentCreateApi(APIView):
#     @swagger_auto_schema(request_body=StudentSerializer)
#     def post(self,request):
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(data=serializer.data)
#         return Response(data=serializer.errors)



class UserStudentCreateApi(APIView):
    @swagger_auto_schema(request_body=StudentSerializer)
    def post(self, request):
        data = {"success": True}
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data["data"] = serializer.data
            return Response(data=data)
        return Response(serializer.errors)

    def get(self, request):
        student = Student.objects.all().order_by('-id')
        serializer = StudentSerializer(student, many=True)
        return Response(data=serializer.data)


# class StudentCrudApi(APIView):
#
#     def get(self, request, pk):
#         response = {"success": True}
#
#         try:
#             student = Student.objects.get(pk=pk)
#             serializer = StudentCrudSerializer(student)
#             response["data"] = serializer.data
#             return Response(data=response)
#         except Teacher.DoesNotExist:
#             response["success"] = False
#             return Response(data=response)
#
#     def put(self, request, pk):
#         response = {"success": True}
#
#         try:
#             student = Student.objects.get(pk=pk)
#             serializer = StudentCrudSerializer(student, data=request.data)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 response["data"] = serializer.data
#                 return Response(data=response)
#             return Response(data=serializer.data)
#         except Student.DoesNotExist:
#             response["success"] = False
#             response["error"] = "Student not found"
#             return Response(data=response, status=status.HTTP_404_NOT_FOUND)
#
#     def patch(self, request, pk):
#         response = {"success": True}
#         try:
#             student = Student.objects.get(pk=pk)
#             serializer = StudentCrudSerializer(student, data=request.data, partial=True)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 response["data"] = serializer.data
#             return Response(data=response, status=status.HTTP_200_OK)
#         except Student.DoesNotExist:
#             response["success"] = False
#             response["error"] = "Student not found"
#             return Response(data=response, status=status.HTTP_404_NOT_FOUND)
#
#     def delete(self, request, pk):
#         response = {"success": True}
#
#         try:
#             student = Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             response["error"] = "bunday malumot yuq"
#             return Response(data=response, status=status.HTTP_417_EXPECTATION_FAILED)
#         id = student.pk
#         student.delete()
#         return Response(data={"id": f"{id} o`chirildi"})
