from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import University, School, Department
from .serializers import UniversitySerializer, SchoolSerializer, DepartmentSerializer

class UniversityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    @action(detail=True, methods=['get'])
    def departments(self, request, pk=None):
        school = self.get_object()
        departments = school.departments.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
