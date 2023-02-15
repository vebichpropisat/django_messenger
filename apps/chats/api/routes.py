from django.urls import path
from . import views

urlpatterns = [
    path("messages/", views.messages_list, name="messages_list"),
]
