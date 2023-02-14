from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.chats.api.serializers import MessageSerializer
from apps.chats.models import Message


@api_view(["GET", "POST"])
def messages_list(request):
    """Messages list api view."""
    if request.method == "GET":
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    serializer = MessageSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    message = serializer.save()
    return Response(data=MessageSerializer(message).data, status=status.HTTP_200_OK)
