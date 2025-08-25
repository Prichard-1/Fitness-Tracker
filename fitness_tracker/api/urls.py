# apps/activities/urls.py
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, UserViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'activities', ActivityViewSet, basename='activity')

urlpatterns = [
    path('', include(router.urls)),
]
