from django.urls import path
from . import views

urlpatterns = [
    path("", views.MessagesAPI.as_view(), name="messages"),
]
