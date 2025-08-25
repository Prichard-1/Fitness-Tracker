from rest_framework import viewsets, generics, filters
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Activity
from .serializers import ActivitySerializer, UserSerializer
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum

# Users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# Activities CRUD
class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [IsOwner]

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['date', 'duration', 'calories_burned']
    search_fields = ['activity_type']

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # Metrics endpoint
    @action(detail=False, methods=['get'])
    def metrics(self, request):
        queryset = self.get_queryset()
        total_duration = queryset.aggregate(Sum('duration'))['duration__sum'] or 0
        total_distance = queryset.aggregate(Sum('distance'))['distance__sum'] or 0
        total_calories = queryset.aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0
        return Response({
            'total_duration': total_duration,
            'total_distance': total_distance,
            'total_calories': total_calories
        })

# Today's activity
class TodayActivityList(generics.ListAPIView):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        today = timezone.now().date()
        return Activity.objects.filter(user=self.request.user, date=today)
