from rest_framework import serializers

from apps.chats.models import Message


class MessageSerializer(serializers.ModelSerializer):
    """Message model serializer."""

    sender = serializers.SerializerMethodField("_get_sender")

    class Meta:
        model = Message
        fields = ("id", "text", "sender", "created_at", "updated_at")

    def _get_sender(self, obj):
        return self.context.get("sender")
