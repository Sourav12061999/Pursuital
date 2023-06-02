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
    path('campaigns/delete/', CampaignDeleteAPIView.as_view(), namw="campaign-delete")
]
