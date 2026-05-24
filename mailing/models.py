from __future__ import annotations

from django.db import models


class NewsletterSubscriber(models.Model):
    LANGUAGE_FR = "fr"
    LANGUAGE_EN = "en"
    LANGUAGE_CHOICES = [
        (LANGUAGE_FR, "Français"),
        (LANGUAGE_EN, "English"),
    ]

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=80, blank=True)
    last_name = models.CharField(max_length=80, blank=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default=LANGUAGE_FR)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=["language"])]

    def __str__(self) -> str:
        return self.email


class NewsletterCampaign(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_SCHEDULED = "scheduled"
    STATUS_RUNNING = "running"
    STATUS_SENT = "sent"
    STATUS_CANCELLED = "cancelled"

    STATUS_CHOICES = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_SCHEDULED, "Scheduled"),
        (STATUS_RUNNING, "Running"),
        (STATUS_SENT, "Sent"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    LANGUAGE_FR = NewsletterSubscriber.LANGUAGE_FR
    LANGUAGE_EN = NewsletterSubscriber.LANGUAGE_EN
    LANGUAGE_CHOICES = NewsletterSubscriber.LANGUAGE_CHOICES

    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default=LANGUAGE_FR)
    subject = models.CharField(max_length=255)
    body = models.TextField()

    scheduled_at = models.DateTimeField()
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=STATUS_SCHEDULED)

    sent_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["language", "scheduled_at"]),
            models.Index(fields=["status"]),
        ]

    def __str__(self) -> str:
        return f"{self.language} - {self.subject[:40]}"


class NewsletterSendLog(models.Model):
    STATUS_QUEUED = "queued"
    STATUS_SENT = "sent"
    STATUS_FAILED = "failed"

    STATUS_CHOICES = [
        (STATUS_QUEUED, "Queued"),
        (STATUS_SENT, "Sent"),
        (STATUS_FAILED, "Failed"),
    ]

    campaign = models.ForeignKey(NewsletterCampaign, on_delete=models.CASCADE, related_name="send_logs")
    subscriber = models.ForeignKey(
        NewsletterSubscriber, on_delete=models.SET_NULL, null=True, blank=True, related_name="send_logs"
    )

    email_to = models.EmailField()
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=STATUS_QUEUED)
    error = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = [
            ("campaign", "email_to"),
        ]
        indexes = [
            models.Index(fields=["campaign", "status"]),
            models.Index(fields=["email_to"]),
        ]

    def __str__(self) -> str:
        return f"{self.email_to} ({self.status})"


class ContactMessage(models.Model):
    LANGUAGE_FR = "fr"
    LANGUAGE_EN = "en"
    LANGUAGE_CHOICES = [
        (LANGUAGE_FR, "Français"),
        (LANGUAGE_EN, "English"),
    ]

    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default=LANGUAGE_FR)

    full_name = models.CharField(max_length=160)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    message = models.TextField()

    is_sent = models.BooleanField(default=False)
    sent_at = models.DateTimeField(null=True, blank=True)
    error = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=["language", "is_sent"])]

    def __str__(self) -> str:
        return f"{self.full_name} ({self.language})"


class ServiceRequest(models.Model):
    LANGUAGE_FR = "fr"
    LANGUAGE_EN = "en"
    LANGUAGE_CHOICES = [
        (LANGUAGE_FR, "Français"),
        (LANGUAGE_EN, "English"),
    ]

    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default=LANGUAGE_FR)

    full_name = models.CharField(max_length=160)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    company = models.CharField(max_length=200, blank=True)
    request_type = models.CharField(max_length=120, blank=True)

    description = models.TextField()

    is_sent = models.BooleanField(default=False)
    sent_at = models.DateTimeField(null=True, blank=True)
    error = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=["language", "is_sent"])]

    def __str__(self) -> str:
        return f"{self.full_name} ({self.language})"
