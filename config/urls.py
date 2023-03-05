from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls.authtoken")),
    path("api/v1/messages/", include("apps.chats.api.routes")),
]
