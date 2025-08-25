from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Activity

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'distance', 'calories_burned', 'date']
