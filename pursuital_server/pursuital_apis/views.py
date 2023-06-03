from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import UserSerializer, BatchSerializer, CampaignSerializer, CampaignUserSerializer, GoalSerializer, GoalUserSerializer, MilestoneSerializer, MilestoneUserSerializer
from .models import Batch , User, Goal, GoalUser, Campaign, CampaignUser, Milestone, MilestoneUser
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
        return super().list(request, *args, **kwargs)

class CampaignUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def put(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)

        campaign_id = kwargs.get('campaign_id')
        campaign = self.get_object()
        # Update the campaign data

        return self.update(request, *args, **kwargs)
class CampaignDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def delete(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)

        campaign_id = kwargs.get('campaign_id')
        campaign = self.get_object()
        # Perform any additional checks or actions before deleting the campaign

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
    serializer_class = CampaignUserSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        campaign_id = self.kwargs.get('campaign_id')
        
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        
        if campaign_id:
            queryset = CampaignUser.objects.filter(campaign_id=campaign_id)
        else:
            queryset = CampaignUser.objects.all()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CampaignUserDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)

        user_id = self.kwargs.get('user_id')
        campaign_id = self.kwargs.get('campaign_id')

        try:
            campaign_user = CampaignUser.objects.get(user_id=user_id, campaign_id=campaign_id)
        except CampaignUser.DoesNotExist:
            return Response("CampaignUser not found", status=status.HTTP_404_NOT_FOUND)

        self.perform_destroy(campaign_user)
        return Response(status=status.HTTP_204_NO_CONTENT)


## Goals
class GoalCreateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, campaign_id):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        
        serializer = GoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(campaign_id=campaign_id)  # Set the campaign ID in the serializer data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GoalListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = GoalSerializer

    def get_queryset(self):
        goal_id = self.kwargs.get('goal_id')
        queryset = Goal.objects.filter(id=goal_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return self.get_paginated_response(serializer.data) if self.paginate_queryset(queryset) else Response(serializer.data)


## GoalUser
class GoalUserCreateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, campaign_user_id, goal_id):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        
        data = {
            'campaign_user': campaign_user_id,
            'goal': goal_id,
            'submission': request.data.get('submission')
        }
        
        serializer = GoalUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GoalUserListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = GoalUser.objects.all()
    serializer_class = GoalUserSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        campaign_id = self.kwargs['campaign_id']
        print(user_id)
        print(campaign_id)
        queryset = GoalUser.objects
        if user_id and campaign_id:
          queryset = GoalUser.objects.filter(campaign_user__user_id=user_id, campaign_user__campaign_id=campaign_id)
        elif user_id:
          queryset = GoalUser.objects.filter(campaign_user__user_id=user_id)
        elif campaign_id:
          queryset = GoalUser.objects.filter(campaign_user__campaign_id=campaign_id)

        return queryset

    def get(self, request, *args, **kwargs):
        user = request.user
        print(user)
        return super().list(request, *args, **kwargs)


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
    serializer_class = MilestoneSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role != "admin":
            return Milestone.objects.none()
        
        milestone_id = self.kwargs.get('milestone_id')
        if milestone_id:
            queryset = Milestone.objects.filter(id=milestone_id)
        else:
            queryset = Milestone.objects.all()

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return self.get_paginated_response(serializer.data) if self.paginate_queryset(queryset) else Response(serializer.data)

class MilestoneUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, milestone_id, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class MilestoneDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, milestone_id, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)

        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

## MilestoneUser
class MilestoneUserCreateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, campaign_user_id, milestone_id):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        
        data = {
            'campaign_user': campaign_user_id,
            'milestone': milestone_id,
            'submission': request.data.get('submission', '')
        }
        
        serializer = MilestoneUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MilestoneUserListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MilestoneUserSerializer

    def get_queryset(self):
        milestone_id = self.request.query_params.get('milestone_id')
        campaign_user_id = self.request.query_params.get('campaignuser_id')

        if milestone_id and campaign_user_id:
            queryset = MilestoneUser.objects.filter(milestone_id=milestone_id, campaign_user_id=campaign_user_id)
        elif milestone_id:
            queryset = MilestoneUser.objects.filter(milestone_id=milestone_id)
        elif campaign_user_id:
            queryset = MilestoneUser.objects.filter(campaign_user_id=campaign_user_id)
        else:
            queryset = MilestoneUser.objects.all()

        return queryset

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        return super().list(request, *args, **kwargs)

class MilestoneUserDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, milestone_user_id):
        user = request.user
        if user.role != "admin":
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)
        
        try:
            milestone_user = MilestoneUser.objects.get(id=milestone_user_id)
        except MilestoneUser.DoesNotExist:
            return Response("Milestone User not found", status=status.HTTP_404_NOT_FOUND)
        
        milestone_user.delete()
        return Response("Milestone User deleted successfully", status=status.HTTP_204_NO_CONTENT)