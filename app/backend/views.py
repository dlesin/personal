from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import User, Department
from .serializers import UserSerializer, DepartmentSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DepartmentViewSet(ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
