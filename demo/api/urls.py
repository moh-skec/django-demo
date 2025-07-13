from django.urls import path
from .views import ApiOverviewView, TaskListCreateView, TaskDetailView

urlpatterns = [
    path('', ApiOverviewView.as_view(), name='api-overview'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]
