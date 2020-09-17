from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import User, Department


class DepartmentSerializer(HyperlinkedModelSerializer):
    users = SerializerMethodField()

    class Meta:
        model = Department
        fields = ('id', 'name', 'timestamp', 'users')

    def get_users(self, obj):
        result = User.objects.filter(department=obj)
        serializer = UserSerializer(result, read_only=True, many=True, context=self.context)
        return serializer.data


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'department', 'description', 'date_joined', 'url', 'avatar',
                  'is_active', 'is_staff', 'is_teamlead', 'is_director', 'is_superuser')
