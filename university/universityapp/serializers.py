from rest_framework import serializers
from .models import University, School, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = School
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    schools = SchoolSerializer(many=True, read_only=True)

    class Meta:
        model = University
        fields = '__all__'