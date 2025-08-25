# apps/activities/views.py
from rest_framework import viewsets, permissions, filters
from .models import Activity
from .serializers import ActivitySerializer, UserSerializer
from .permissions import IsOwner
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum

# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admin can list users

# Activity ViewSet
class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['activity_type']
    ordering_fields = ['date', 'duration', 'calories_burned']

    def get_queryset(self):
        # Only return activities of the logged-in user
        user = self.request.user
        queryset = Activity.objects.filter(user=user)
        
        # Optional filters: by date range
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        activity_type = self.request.query_params.get('activity_type')
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])
        if activity_type:
            queryset = queryset.filter(activity_type=activity_type)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def summary(self, request):
        """
        Return total duration, distance, calories for the user
        """
        activities = self.get_queryset()
        total_duration = activities.aggregate(Sum('duration'))['duration__sum'] or 0
        total_distance = activities.aggregate(Sum('distance'))['distance__sum'] or 0
        total_calories = activities.aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0
        return Response({
            "total_duration": total_duration,
            "total_distance": total_distance,
            "total_calories": total_calories
        })
