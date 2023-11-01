# pylint: disable=import-error
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import permissions
from todo.models import Task
from .serializers import TaskSerializer
User = get_user_model()

class TodoViewSet(viewsets.ModelViewSet):
    """
      to get all
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
     
    
