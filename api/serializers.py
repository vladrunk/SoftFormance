from abc import ABCMeta

from rest_framework import serializers

from django.contrib.auth.models import User
from feed.models import FeedItem, RegisteredUser


class FeedItemSerializers(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    content = serializers.CharField(read_only=True)

    class Meta:
        model = FeedItem
        fields = 'user', 'content'


class UsernameSerializers(serializers.ModelSerializer):
    def to_representation(self, instance):
        return f'{instance}'

    class Meta:
        model = RegisteredUser
        fields = 'user',


class TrackingField(serializers.RelatedField, metaclass=ABCMeta):
    def get_queryset(self):
        return RegisteredUser.objects.all().order_by('user__pk')

    def to_representation(self, obj):
        return f'{obj.user.username}'

    def to_internal_value(self, data):
        return RegisteredUser.objects.get(user__username=data)


class RegisteredUserSerializers(serializers.ModelSerializer):
    username = UsernameSerializers(read_only=True, source='user')
    user = serializers.CharField(max_length=255, write_only=True)
    tracking = TrackingField(many=True)

    def create(self, validated_data):
        user, new = User.objects.get_or_create(username=validated_data['user'])
        if new:
            reg_user = RegisteredUser.objects.get_or_create(user=user)[0]
            reg_user.tracking.add(*validated_data['tracking'])
            return reg_user
        else:
            return RegisteredUser.objects.get(user=user)

    class Meta:
        model = RegisteredUser
        fields = ['id', 'username', 'user', 'tracking']
