from django.urls import path
from .views import UserDetailView, BatchCreateAPIView, BatchListAPIView, SignupView, SigninView, CampaignCreateAPIView, CampaignListAPIView, CampaignUpdateAPIView, CampaignDeleteAPIView, CampaignUserCreateAPIView, CampaignUserListAPIView, CampaignUserDeleteAPIView, GoalCreateAPIView, GoalListAPIView, GoalUpdateAPIView, GoalDeleteAPIView, GoalUserCreateAPIView, GoalUserListAPIView, GoalUserUpdateAPIView, GoalUserDeleteAPIView, MilestoneCreateAPIView, MilestoneListAPIView, MilestoneUpdateAPIView, MilestoneDeleteAPIView, MilestoneUserCreateAPIView, MilestoneUserListAPIView, MilestoneUserUpdateAPIView, MilestoneUserDeleteAPIView



urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('batches/list/', BatchListAPIView.as_view(), name='batch-list'),
    path('batches/create/', BatchCreateAPIView.as_view(), name='batch-create'),
    path('campaigns/create/', CampaignCreateAPIView.as_view(), name="campaign-create"),
    path('campaigns/list/', CampaignListAPIView.as_view(), name="campaign-list"),
    path('campaigns/update/<int:campaign_id>', CampaignUpdateAPIView.as_view(), name="campaign-update"),
    path('campaigns/delete/<int:campaign_id>', CampaignDeleteAPIView.as_view(), name="campaign-delete"),

    # CampaignUser routes
    path('campaigns-users/create/', CampaignUserCreateAPIView.as_view(), name="campaign-user-create"),
    path('campaigns-users/list/<int:campaign_id>/', CampaignUserListAPIView.as_view(), name="campaign-user-list"),
    path('campaigns-users/delete/<int:user_id>/<int:campaign_id>/', CampaignUserDeleteAPIView.as_view(), name="campaign-user-delete"),

    # Goal routes
    path('goals/create/<int:campaign_id>/', GoalCreateAPIView.as_view(), name="goals-create"),
    path('goals/list/<int:goal_id>/', GoalListAPIView.as_view(), name="goals-list"),
    # GoalUser routes
    path('goals-users/create/', GoalUserCreateAPIView.as_view(), name="goal-user-create"),
    path('goals-users/list/', GoalUserListAPIView.as_view(), name="goal-user-list"),
    path('goals-users/update/', GoalUserUpdateAPIView.as_view(), name="goal-user-update"),
    path('goals-users/delete/', GoalUserDeleteAPIView.as_view(), name="goal-user-delete"),

    # Milestone routes
    path('milestones/create/', MilestoneCreateAPIView.as_view(), name="milestone-create"),
    path('milestones/list/', MilestoneListAPIView.as_view(), name="milestone-list"),
    path('milestones/update/', MilestoneUpdateAPIView.as_view(), name="milestone-update"),
    path('milestones/delete/', MilestoneDeleteAPIView.as_view(), name="milestone-delete"),

    # MilestoneUser routes
    path('milestones-users/create/', MilestoneUserCreateAPIView.as_view(), name="milestone-user-create"),
    path('milestones-users/list/', MilestoneUserListAPIView.as_view(), name="milestone-user-list"),
    path('milestones-users/update/', MilestoneUserUpdateAPIView.as_view(), name="milestone-user-update"),
    path('milestones-users/delete/', MilestoneUserDeleteAPIView.as_view(), name="milestone-user-delete"),

]
