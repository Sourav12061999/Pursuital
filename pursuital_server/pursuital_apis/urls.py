from django.urls import path
from .views import UserDetailView, BatchCreateAPIView, BatchListAPIView, SignupView, SigninView, CampaignCreateAPIView, CampaignListAPIView, CampaignUpdateAPIView, CampaignDeleteAPIView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('batches/list/', BatchListAPIView.as_view(), name='batch-list'),
    path('batches/create/', BatchCreateAPIView.as_view(), name='batch-create'),
    path('campaigns/create/', CampaignCreateAPIView.as_view(), namw="campaign-create"),
    path('campaigns/list/', CampaignListAPIView.as_view(), namw="campaign-list"),
    path('campaigns/update/', CampaignUpdateAPIView.as_view(), namw="campaign-update"),
    path('campaigns/delete/', CampaignDeleteAPIView.as_view(), namw="campaign-delete"),
    # CampaignUser routes
    path('campaigns/users/create/', CampaignUserCreateAPIView.as_view(), name="campaign-user-create"),
    path('campaigns/users/list/', CampaignUserListAPIView.as_view(), name="campaign-user-list"),
    path('campaigns/users/update/', CampaignUserUpdateAPIView.as_view(), name="campaign-user-update"),
    path('campaigns/users/delete/', CampaignUserDeleteAPIView.as_view(), name="campaign-user-delete"),

    # Goal routes
    path('goals/create/', GoalCreateAPIView.as_view(), name="goal-create"),
    path('goals/list/', GoalListAPIView.as_view(), name="goal-list"),
    path('goals/update/', GoalUpdateAPIView.as_view(), name="goal-update"),
    path('goals/delete/', GoalDeleteAPIView.as_view(), name="goal-delete"),

    # GoalUser routes
    path('goals/users/create/', GoalUserCreateAPIView.as_view(), name="goal-user-create"),
    path('goals/users/list/', GoalUserListAPIView.as_view(), name="goal-user-list"),
    path('goals/users/update/', GoalUserUpdateAPIView.as_view(), name="goal-user-update"),
    path('goals/users/delete/', GoalUserDeleteAPIView.as_view(), name="goal-user-delete"),

    # Milestone routes
    path('milestones/create/', MilestoneCreateAPIView.as_view(), name="milestone-create"),
    path('milestones/list/', MilestoneListAPIView.as_view(), name="milestone-list"),
    path('milestones/update/', MilestoneUpdateAPIView.as_view(), name="milestone-update"),
    path('milestones/delete/', MilestoneDeleteAPIView.as_view(), name="milestone-delete"),

    # MilestoneUser routes
    path('milestones/users/create/', MilestoneUserCreateAPIView.as_view(), name="milestone-user-create"),
    path('milestones/users/list/', MilestoneUserListAPIView.as_view(), name="milestone-user-list"),
    path('milestones/users/update/', MilestoneUserUpdateAPIView.as_view(), name="milestone-user-update"),
    path('milestones/users/delete/', MilestoneUserDeleteAPIView.as_view(), name="milestone-user-delete"),

]
