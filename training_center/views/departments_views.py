from rest_framework.viewsets import ModelViewSet

from ..models import *
from ..serializers import *


class DepartmentsViewSet(ModelViewSet):

    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer

class CourseViewSet(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer