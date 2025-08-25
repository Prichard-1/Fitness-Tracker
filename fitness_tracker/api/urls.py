from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, UserViewSet, UserSignupView, TodayActivityList

router = DefaultRouter()
router.register('activities', ActivityViewSet, basename='activities')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('activities/today/', TodayActivityList.as_view({'get':'list'}), name='activities-today'),
    path('', include(router.urls)),
]
