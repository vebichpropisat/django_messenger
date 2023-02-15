from rest_framework import serializers

from apps.chats.models import Message


class MessageSerializer(serializers.ModelSerializer):
    """Message model serializer."""

    class Meta:
        model = Message
        fields = ("id", "text", "sender", "created_at", "updated_at")
