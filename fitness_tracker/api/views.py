from rest_framework import viewsets, generics, permissions
from django.contrib.auth.models import User        # <-- Add this
from .models import Activity
from .serializers import ActivitySerializer, UserSerializer, UserSignupSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone

# -----------------------------
# Activity CRUD ViewSet
# -----------------------------
class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return only the activities of the logged-in user
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the logged-in user to the activity
        serializer.save(user=self.request.user)


# -----------------------------
# User CRUD ViewSet (optional)
# -----------------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can see all users


# -----------------------------
# Signup View
# -----------------------------
class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can sign up


# -----------------------------
# Today’s Activities List
# -----------------------------
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone

class TodayActivityList(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def list(self, request):
        today = timezone.now().date()
        activities = Activity.objects.filter(user=request.user, date=today)
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
