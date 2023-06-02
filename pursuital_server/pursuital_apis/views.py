from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, BatchSerializer
from .models import Batch
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class SignupView(APIView):
    def post(self, request):
        request.data["role"] = "student"
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SigninView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        # Authenticate user
        user = authenticate(email=email, password=password)
        
        if user is not None:
            # Generate or retrieve the authentication token
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class UserDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # Here you can access the user object and retrieve its data
        # For example:
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': user.role
        }
        return Response(user_data, status=status.HTTP_200_OK)

class BatchListAPIView(generics.ListAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BatchCreateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)