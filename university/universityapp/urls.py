from rest_framework.routers import DefaultRouter
from .views import UniversityViewSet, SchoolViewSet, DepartmentViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'universities', UniversityViewSet, basename='university')
router.register(r'schools', SchoolViewSet, basename='school')
router.register(r'departments', DepartmentViewSet, basename='department')

urlpatterns = [
    path('api/', include(router.urls)),
]