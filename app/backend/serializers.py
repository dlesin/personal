from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, HyperlinkedModelSerializer
from .models import User


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'date_joined', 'url')

