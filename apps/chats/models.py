from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Message(models.Model):
    """Message model."""

    text = models.TextField(max_length=1000)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")

    def __str__(self) -> str:
        """Return message identifier string."""
        return f"Message #{self.pk} by {self.sender}."
