from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class University(models.Model):
    university_id = models.AutoField(primary_key=True)
    university_name = models.CharField(max_length=255)
    university_code = models.CharField(max_length=50, unique=True)
    establishment_year = models.CharField(max_length=10)
    accreditation = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField()
    contact_info = models.TextField()
    website = models.URLField(blank=True, null=True)
    governance_structure = models.JSONField(blank=True, null=True)
    policies = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.university_name


class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    university = models.ForeignKey(University, related_name='schools', on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255)
    school_code = models.CharField(max_length=50, unique=True)
    school_type = models.CharField(max_length=100)
    establishment_year = models.CharField(max_length=10)
    accreditation = models.CharField(max_length=255, blank=True, null=True)
    dean = models.ForeignKey(User, related_name='dean_schools', on_delete=models.SET_NULL, null=True, blank=True)
    facilities = models.JSONField(blank=True, null=True)
    vision_mission = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.school_name


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    school = models.ForeignKey(School, related_name='departments', on_delete=models.CASCADE)
    department_name = models.CharField(max_length=255)
    department_code = models.CharField(max_length=50, unique=True)
    department_type = models.CharField(max_length=100)
    hod = models.ForeignKey(User, related_name='hod_departments', on_delete=models.SET_NULL, null=True, blank=True)
    research_areas = models.JSONField(blank=True, null=True)
    facilities = models.JSONField(blank=True, null=True)
    collaborations = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name
