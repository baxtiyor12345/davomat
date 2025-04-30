from ..models import *
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=["title", "is_active", "descriptions"]


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Table
        fields="__all__"

class TableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=TableType
        fields="__all__"


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rooms
        fields="__all__"

class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Parents
        fields="__all__"

