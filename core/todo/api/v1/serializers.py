# pylint: disable=import-error
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
from django.contrib.auth import get_user_model
from rest_framework import serializers
from todo.models import Task



class UserSerialzier(serializers.ModelSerializer):    

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class TaskSerializer(serializers.ModelSerializer):
    # snipeet= serializers.ReadOnlyField(source="get_snippet")
    user = UserSerialzier(read_only=True)  # Include the nested serializer
    # read_only_fields = ['username']
    class Meta:
        model = Task       
        fields = ["id","title", "complete","user"]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return Task.objects.create(**validated_data)