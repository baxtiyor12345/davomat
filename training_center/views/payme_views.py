from rest_framework import status
from rest_framework.response import Response

from ..serializers.payme_serializer import PaymeSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from ..models.payme_model import *

class PaymeApi(APIView):
    @swagger_auto_schema(responses={200:PaymeSerializer(many=True)})
    def get(self,request):
        payme=Payme.objects.all()
        serializer=PaymeSerializer(payme, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=PaymeSerializer)
    def post(self,request):
        serializer=PaymeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

