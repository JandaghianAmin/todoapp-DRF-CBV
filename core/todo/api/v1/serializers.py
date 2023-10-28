# pylint: disable=import-error
from rest_framework import serializers
from todo.models import Task
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

user = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    snipeet= serializers.ReadOnlyField(source="get_snippet")
    
    class Meta:
        model = Task
        read_only_fields = ('user',)
        fields = ["id","user","title","complete","snipeet"]

  

class UserSerialzier(serializers.ModelSerializer):
    todos = TaskSerializer(read_only=True, many=True)

    class Meta:
        model = user
        fields = ["id","username","is_active","todos"]      