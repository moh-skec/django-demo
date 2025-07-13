from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class TaskListCreateView(generics.ListCreateAPIView):
    """
    List all tasks or create a new task
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a task
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class ApiOverviewView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        """
        API overview endpoint
        """
        api_urls = {
            'Overview': '/api/',
            'Task List': '/api/tasks/',
            'Task Detail': '/api/tasks/<int:pk>/',
            'Create Task': '/api/tasks/ (POST)',
            'Update Task': '/api/tasks/<int:pk>/ (PUT/PATCH)',
            'Delete Task': '/api/tasks/<int:pk>/ (DELETE)',
        }
        return Response(api_urls)
