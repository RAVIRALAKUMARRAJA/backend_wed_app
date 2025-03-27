from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListView(APIView):
    permission_classes = [AllowAny]  # No authentication required

    def get(self, request):
        ...
