from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    ContactInfoView,
    ContactMessageViewSet,
    NewsletterCampaignViewSet,
    NewsletterSendLogViewSet,
    NewsletterSubscriberViewSet,
    ServiceRequestViewSet,
)

router = DefaultRouter()
router.register(r"subscribers", NewsletterSubscriberViewSet, basename="subscribers")
router.register(r"campaigns", NewsletterCampaignViewSet, basename="campaigns")
router.register(r"campaigns/send-logs", NewsletterSendLogViewSet, basename="campaign-send-logs")
router.register(r"contact", ContactMessageViewSet, basename="contact")
router.register(r"service-requests", ServiceRequestViewSet, basename="service-requests")

urlpatterns = router.urls + [
    path("contact-info/", ContactInfoView.as_view(), name="contact-info"),
]
