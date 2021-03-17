from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'api/users', views.RegisteredUserViewSet, basename='users')
router.register(r'api/feed/all', views.FeedAllViewSet, basename='feed_all')
router.register(r'api/feed/subs', views.FeedSubsViewSet, basename='feed_subs')
router.register(r'api/feed', views.FeedViewSet, basename='feed_own')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
