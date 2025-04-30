from ..models.payme_model import *
from rest_framework import serializers


class PaymeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Payme
        fields="__all__"


