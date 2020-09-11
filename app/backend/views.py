from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import UserSerializer
from .models import User


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
