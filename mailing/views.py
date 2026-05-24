from __future__ import annotations

from django.conf import settings
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    ContactMessage,
    NewsletterCampaign,
    NewsletterSendLog,
    NewsletterSubscriber,
    ServiceRequest,
)
from .serializers import (
    ContactMessageSerializer,
    NewsletterCampaignSerializer,
    NewsletterSendLogSerializer,
    NewsletterSubscriberSerializer,
    ServiceRequestSerializer,
)
from .tasks import (
    send_contact_message,
    send_due_newsletters,
    send_newsletter_campaign,
    send_service_request,
)


class NewsletterSubscriberViewSet(viewsets.ModelViewSet):
    queryset = NewsletterSubscriber.objects.all().order_by("-created_at")
    serializer_class = NewsletterSubscriberSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get", "post", "head", "options"]


class NewsletterCampaignViewSet(viewsets.ModelViewSet):
    queryset = NewsletterCampaign.objects.all().order_by("-scheduled_at")
    serializer_class = NewsletterCampaignSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get", "post", "head", "options"]

    @action(detail=True, methods=["post"], url_path="send")
    def send_now(self, request, pk: str | None = None) -> Response:
        campaign = self.get_object()
        send_newsletter_campaign.delay(campaign.id)
        return Response({"detail": "newsletter campaign send triggered", "campaign_id": campaign.id})

    @action(detail=False, methods=["post"], url_path="send-due")
    def send_due_now(self, request) -> Response:
        # En dev/eager, apply().get() donne immédiatement le nombre de campagnes déclenchées.
        result = send_due_newsletters.apply()
        count = result.get()
        return Response({"detail": "due newsletters send triggered", "campaigns_due_count": count})


class NewsletterSendLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewsletterSendLog.objects.all().order_by("-created_at")
    serializer_class = NewsletterSendLogSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get", "head", "options"]


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by("-created_at")
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ["post", "get", "head", "options"]

    def perform_create(self, serializer: ContactMessageSerializer) -> None:
        obj = serializer.save()
        send_contact_message.delay(obj.id)


class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all().order_by("-created_at")
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ["post", "get", "head", "options"]

    def perform_create(self, serializer: ServiceRequestSerializer) -> None:
        obj = serializer.save()
        send_service_request.delay(obj.id)


class ContactInfoView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request) -> Response:
        return Response(
            {
                "email": getattr(settings, "DEFAULT_FROM_EMAIL", "") or "",
                "phone_fr": getattr(settings, "NCE_PHONE_FR", "") or "",
                "phone_cm": getattr(settings, "NCE_PHONE_CM", "") or "",
            }
        )
