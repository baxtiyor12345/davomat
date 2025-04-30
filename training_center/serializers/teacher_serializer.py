from rest_framework import serializers
from ..models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .auth_serializer import *


# class UserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("phone_number", "password", "email")
#
#     def create(self, validated_data):
#         validated_data["is_teacher"] = True
#         validated_data["is_active"] = True
#         return User.objects.create_user(**validated_data)


class TeacherSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    course=serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)
    departments=serializers.PrimaryKeyRelatedField(queryset=Departments.objects.all(), many=True)

    class Meta:
        model=Teacher
        fields=["id","user","departments","course","descriptions"]

    def create(self, validated_data):
        user_db=validated_data.pop("user")
        user_db["is_teacher"]=True
        user_db["is_active"]=True
        course_db=validated_data.pop("course")
        departments_db=validated_data.pop("departments")
        user=User.objects.create_user(**user_db)
        teacher=Teacher.objects.create(user=user, **validated_data)
        teacher.course.set(course_db)
        teacher.departments.set(departments_db)
        return teacher
