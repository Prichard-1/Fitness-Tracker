from rest_framework import viewsets, generics, permissions, filters
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import render  # ✅ Moved to top for clarity

from .models import Activity
from .serializers import ActivitySerializer, UserSerializer
from .permissions import IsOwner

# 👤 User CRUD
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # ✅ Allows open registration

# 🏃 Activity CRUD
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()  # ✅ Added to satisfy DRF router
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['date', 'duration', 'calories_burned']
    search_fields = ['activity_type']

    def get_queryset(self):
        # ✅ Scoped to current user
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # ✅ Automatically assign owner
        serializer.save(user=self.request.user)

# 📅 View today’s activity history
class TodayActivityList(generics.ListAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        today = timezone.now().date()
        return Activity.objects.filter(user=self.request.user, date=today)
