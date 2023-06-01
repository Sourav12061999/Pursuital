from pursuital_apis.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics

User = get_user_model()


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
