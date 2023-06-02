from rest_framework import serializers
from .models import Batch, User, Campaign, CampaignUser, Goal, GoalUser, Milestone, MilestoneUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['id', 'name', 'type']


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['id', 'name', 'start_date', 'end_date', 'progress', 'link_identifier', 'description',
                  'cover_photo', 'status']


class CampaignUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignUser
        fields = ['id', 'user', 'campaign', 'enrollment_date', 'status']


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'title', 'date', 'type']


class GoalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalUser
        fields = ['id', 'campaign_user', 'goal', 'submission']


class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = ['id', 'name', 'goal_count']


class MilestoneUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilestoneUser
        fields = ['id', 'milestone', 'achievement_date']

