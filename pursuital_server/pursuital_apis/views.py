from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import UserSerializer, BatchSerializer, CampaignSerializer, CampaignUserSerializer, GoalSerializer, GoalUserSerializer, MilestoneSerializer, MilestoneUserSerializer
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
        print(user.batch)
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': user.role,
            'student_id': user.student_id,
            'batch': {
               'id': user.batch.id,
               'name': user.batch.name,
               'type': user.batch.type
            },
            'profile_image': user.profile_image
        }
        return Response(user_data, status=status.HTTP_200_OK)

## Batch
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


## Campaigns
class CampaignCreateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampaignListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return super().list(request, *args, **kwargs)

class CampaignUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return self.update(request, *args, **kwargs)

class CampaignDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return self.destroy(request, *args, **kwargs)


## Campaign User
class CampaignUserCreateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        
        serializer = CampaignUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampaignUserListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CampaignUser.objects.all()
    serializer_class = CampaignUserSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return super().list(request, *args, **kwargs)


class CampaignUserUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return self.update(request, *args, **kwargs)


class CampaignUserDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return self.destroy(request, *args, **kwargs)

## Goals
class GoalCreateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        
        serializer = GoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoalListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return super().list(request, *args, **kwargs)


class GoalUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return self.update(request, *args, **kwargs)


class GoalDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return self.destroy(request, *args, **kwargs)


# Similarly, you can define the views for the remaining serializers (, , ) in a similar format.

## GoalUser
class GoalUserCreateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        
        serializer = GoalUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoalUserListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = GoalUser.objects.all()
    serializer_class = GoalUserSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return super().list(request, *args, **kwargs)


class GoalUserUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return self.update(request, *args, **kwargs)


class GoalUserDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return self.destroy(request, *args, **kwargs)

## Milestone
class MilestoneCreateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        
        serializer = MilestoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MilestoneListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return super().list(request, *args, **kwargs)


class MilestoneUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return self.update(request, *args, **kwargs)


class MilestoneDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return self.destroy(request, *args, **kwargs)

## MilestoneUser
class MilestoneUserCreateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        
        serializer = MilestoneUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MilestoneUserListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = MilestoneUser.objects.all()
    serializer_class = MilestoneUserSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return super().list(request, *args, **kwargs)


class MilestoneUserUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return self.update(request, *args, **kwargs)


class MilestoneUserDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return self.destroy(request, *args, **kwargs)
