from rest_framework import viewsets
from sample.models.user import User
from sample.serializers.user import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer