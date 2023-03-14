from rest_framework import serializers

from apps.chats.models import Message


class MessageSerializer(serializers.ModelSerializer):
    """Message model serializer."""

    class Meta:
        model = Message
        fields = ("id", "text", "sender", "created_at", "updated_at")

    def create(self, validated_data):
        sender_id = self.context["sender"]
        message = Message.objects.create(sender_id=sender_id, **validated_data)
        print(self.context)
        return message
