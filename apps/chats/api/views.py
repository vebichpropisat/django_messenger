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
            data=request.data, context={"sender": request.user.pk}
        )
        serializer.is_valid(raise_exception=True)
        message = serializer.save()
        return Response(data=MessageSerializer(message).data, status=status.HTTP_200_OK)

    def get_queryset(self):
        if since_date := self.request.GET.get("created_at"):
            return Message.objects.filter(date_created__gte=since_date)
        return Message.objects.all()
