from rest_framework import serializers
from ..models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .auth_serializer import *

# class StudentUserSerializer(serializers.ModelSerializer):
#     # is_line = serializers.BooleanField(read_only=True)
#     is_active = serializers.BooleanField(read_only=True)
#     is_teacher = serializers.BooleanField(read_only=True)
#     is_admin = serializers.BooleanField(read_only=True)
#     is_student = serializers.BooleanField(read_only=True)
#     is_staff = serializers.BooleanField(read_only=True)
#
#     class Meta:
#         model = User
#         fields = (
#         'id', 'phone_number', 'password', 'email', 'is_active', 'is_teacher', 'is_staff', 'is_admin', 'is_student')

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_number", "password", "email")

    def create(self, validated_data):
        validated_data["is_student"] = True
        validated_data["is_active"] = True
        return User.objects.create_user(**validated_data)


class StudentSerializer(serializers.ModelSerializer):
    user=UserCreateSerializer()
    group=serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)

    class Meta:
        model=Student
        fields=["id","user","group","is_line","descriptions"]

    def create(self, validated_data):
        user_db=validated_data.pop("user")
        user_db["is_student"]=True
        user_db["is_active"]=True
        group_db=validated_data.pop("group")
        user=User.objects.create_user(**user_db)
        student=Student.objects.create(user=user, **validated_data)
        student.group.set(group_db)
        return student




