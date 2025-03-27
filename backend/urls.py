from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

def home(request):
    return HttpResponse("Welcome to the Task Manager API")

urlpatterns = [
    path('api/', include('users.urls')),
    path('admin/', admin.site.urls),
    
    path("", include("tasks.urls")),

    # Authentication (JWT)
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),

    # ✅ Ensure proper API routes
    path("api/users/", include("users.urls")),  
    path("api/adminpanel/", include("adminpanel.urls")),
    path("api/tasks/", include("tasks.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
