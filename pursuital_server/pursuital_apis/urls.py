from django.urls import path, include
from pursuital_apis.views import UserCreateAPIView, UserDetailAPIView

urlpatterns = [
    path(
        "api/accounts/",
        include(
            [
                path("signup/", UserCreateAPIView.as_view(), name="signup"),
                path("user/<int:pk>/", UserDetailAPIView.as_view(), name="user-detail"),
            ]
        ),
    ),
]
