from rest_framework.viewsets import ModelViewSet
from ..models import *
from ..serializers import *


class DepartmentsViewSet(ModelViewSet):

    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer

class CourseViewSet(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RoomsViewSet(ModelViewSet):

    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class TableViewSet(ModelViewSet):

    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableTypeViewSet(ModelViewSet):

    queryset =TableType.objects.all()
    serializer_class = TableTypeSerializer

class ParentsViewSet(ModelViewSet):

    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer

