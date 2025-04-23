from django.urls import path, include
from .views import *
from .views.davomat_views import TeacherDavomatiApi
from .views.login_view import PhoneSendOtp
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('departments', DepartmentsViewSet)
router.register('course', CourseViewSet)
urlpatterns=[
    path("", include(router.urls)),
    path('phone/', PhoneSendOtp.as_view()),
    path('teacher/', TeacherCreateApi.as_view()),
    path('student/', UserStudentCreateApi.as_view()),
    path('group/', GroupApi.as_view()),
    path('teacher_davomati/', TeacherDavomatiApi.as_view()),
    path('student_davomati/', StudentDavomatiApi.as_view())
]