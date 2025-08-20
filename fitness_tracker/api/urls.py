from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ActivityViewSet, TodayActivityList
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'activities', ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('activities/today/', TodayActivityList.as_view(), name='today-activities'),
]

