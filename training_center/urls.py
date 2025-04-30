from django.urls import path, include
from .views import *
from .views.davomat_views import *
from .views.login_view import PhoneSendOtp
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('departments', DepartmentsViewSet)
router.register('course', CourseViewSet)
router.register('rooms', RoomsViewSet)
router.register('table', TableViewSet)
router.register('tabletype', TableTypeViewSet)
router.register('parents', ParentsViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'attendances', AttendanceViewSet)
# router.register('student_davomati/', GroupViewSet)
urlpatterns=[
    path("", include(router.urls)),
    path('phone/', PhoneSendOtp.as_view()),
    path('teacher/', TeacherCreateApi.as_view()),
    path('student/', UserStudentCreateApi.as_view()),
    path('group/', GroupApi.as_view()),
    # path('teacher_davomati/', TeacherDavomatiApi.as_view()),
    # path('student_davomati/', StudentDavomatiApi.as_view()),
    # path('student_davomati/', GroupViewSet),
    path('payme/', PaymeApi.as_view())
]