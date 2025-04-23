from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from ..serializers import *
from training_center.models import Teacher
from training_center.serializers import *

class StudentDavomatiApi(APIView):
    @swagger_auto_schema(request_body=DavomatCreateSerializer)
    def post(self, request):
        serializer = DavomatCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        davomat = serializer.save()
        data = {
            "success": True,
            "data": {
                "id": davomat.id,
                "date": davomat.date,
                "group": davomat.group.id,
                "descriptions": davomat.descriptions
            }
        }
        return Response(data=data, status=201)

    def get(self, request):
        student_davomat = StudentDavomati.objects.all().order_by('-id')
        serializer = StudentDavomatSerializer(student_davomat, many=True)
        return Response(data=serializer.data)



class TeacherDavomatiApi(APIView):
    @swagger_auto_schema(request_body=TeacherCreateSerializer)
    def post(self, request):
        serializer = TeacherCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        davomat = serializer.save()
        data = {
            "success": True,
            "data": {
                "id": davomat.id,
                "date": davomat.date,
                "group": davomat.group.id,
                "descriptions": davomat.descriptions
            }
        }
        return Response(data=data, status=201)

    def get(self, request):
        teacher_davomat = TeacherDavomati.objects.all().order_by('-id')
        serializer = TeacherDavomatSerializer(teacher_davomat, many=True)
        return Response(data=serializer.data)
