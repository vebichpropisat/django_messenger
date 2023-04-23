from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.chats.api.serializers import MessageSerializer
from apps.chats.models import Message


class MessagesAPI(generics.ListCreateAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        serializer = MessageSerializer(
            data=dict(sender=request.user.pk, **request.data.dict())
        )
        serializer.is_valid(raise_exception=True)
        message = serializer.save()
        return Response(data=MessageSerializer(message).data, status=status.HTTP_200_OK)

    def get_queryset(self):
        if since_date := self.request.GET.get("after"):
            return Message.objects.filter(created_at__gt=since_date)
        return Message.objects.all()
