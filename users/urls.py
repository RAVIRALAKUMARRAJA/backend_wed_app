from django.urls import path
from .views import UserProfileView
from .views import protected_view, user_dashboard
from .views import LoginView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path("", user_dashboard, name="user_dashboard"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Get Access & Refresh Token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Get New Access Token
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Verify Token
    path('some-protected-endpoint/', protected_view, name='protected-endpoint'),
    path("", UserProfileView.as_view(), name="user-profile"),
    
]
