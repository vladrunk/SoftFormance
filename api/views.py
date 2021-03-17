from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisteredUserSerializers, FeedItemSerializers
from feed.models import RegisteredUser, FeedItem


class RegisteredUserViewSet(viewsets.ModelViewSet):
    queryset = RegisteredUser.objects.all()
    serializer_class = RegisteredUserSerializers


class FeedAllViewSet(viewsets.ModelViewSet):
    queryset = FeedItem.objects.all()
    serializer_class = FeedItemSerializers


class FeedViewSet(viewsets.ModelViewSet):
    serializer_class = FeedItemSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FeedItem.objects.filter(user=self.request.user)


class FeedSubsViewSet(viewsets.ModelViewSet):
    serializer_class = FeedItemSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        users = [RegisteredUser.objects.get(user=self.request.user)]
        users.extend(self.request.user.registereduser.tracking.all())
        feeds = FeedItem.objects.filter(user__registereduser__in=users).order_by('-pk')
        return feeds
