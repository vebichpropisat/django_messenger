from rest_framework import serializers

from apps.chats.models import Message


class MessageSerializer(serializers.ModelSerializer):
    """Message model serializer."""

    sender_name = serializers.CharField(source="sender.username", read_only=True)

    class Meta:
        model = Message
        fields = ("id", "text", "sender", "sender_name", "created_at", "updated_at")
