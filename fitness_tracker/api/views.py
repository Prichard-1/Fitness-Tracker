from rest_framework import viewsets, generics, permissions, filters
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Activity
from .serializers import ActivitySerializer, UserSerializer
from .permissions import IsOwner

# User CRUD
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # For registration, we allow anyone

# Activity CRUD
class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['date', 'duration', 'calories_burned']
    search_fields = ['activity_type']

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# View today’s activity history
class TodayActivityList(generics.ListAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        today = timezone.now().date()
        return Activity.objects.filter(user=self.request.user, date=today)
from django.shortcuts import render

# Create your views here.
