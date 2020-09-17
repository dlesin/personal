from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, DepartmentViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]