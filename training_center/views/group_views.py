from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from ..models import *
from ..serializers import *

class GroupApi(APIView):
    @swagger_auto_schema(request_body=GroupSerializer)
    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

    def get(self, request):
        users = Group.objects.all().order_by('-id')
        serializer = GroupSerializer(users, many=True)
        return Response(data=serializer.data)


