from todo.models import Task
from .serializers import TaskSerializer, UserSerialzier
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth import get_user_model

User = get_user_model()


class TodoViewSet(viewsets.ModelViewSet):
    """
      to get all
    """
    queryset = Task.objects.order_by("id").all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically associate the current user with the object
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        
    

class UsersGenericApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialzier
    permission_classes = [permissions.IsAuthenticated]
