from django.urls import path
from .views import UserDetailView, BatchCreateAPIView, BatchListAPIView, SignupView, SigninView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('batches/list/', BatchListAPIView.as_view(), name='batch-list'),
    path('batches/create/', BatchCreateAPIView.as_view(), name='batch-create'),
]
