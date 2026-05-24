from __future__ import annotations

from rest_framework import serializers

from .models import (
    ContactMessage,
    NewsletterCampaign,
    NewsletterSendLog,
    NewsletterSubscriber,
    ServiceRequest,
)


class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "language",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "is_active"]

    def validate_language(self, value: str) -> str:
        value = value.lower().strip()
        valid = {choice[0] for choice in NewsletterSubscriber.LANGUAGE_CHOICES}
        if value not in valid:
            raise serializers.ValidationError(f"language must be one of: {sorted(valid)}")
        return value

    def create(self, validated_data: dict) -> NewsletterSubscriber:
        # "email" is unique; if already exists, we just re-activate + update basic fields.
        subscriber, _created = NewsletterSubscriber.objects.get_or_create(email=validated_data["email"])
        subscriber.first_name = validated_data.get("first_name", "") or ""
        subscriber.last_name = validated_data.get("last_name", "") or ""
        subscriber.language = validated_data.get("language", NewsletterSubscriber.LANGUAGE_FR)
        subscriber.is_active = True
        subscriber.save()
        return subscriber


class NewsletterCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterCampaign
        fields = [
            "id",
            "language",
            "subject",
            "body",
            "scheduled_at",
            "status",
            "sent_at",
            "created_at",
        ]
        read_only_fields = ["id", "status", "sent_at", "created_at"]

    def validate_language(self, value: str) -> str:
        value = value.lower().strip()
        valid = {choice[0] for choice in NewsletterCampaign.LANGUAGE_CHOICES}
        if value not in valid:
            raise serializers.ValidationError(f"language must be one of: {sorted(valid)}")
        return value


class NewsletterSendLogSerializer(serializers.ModelSerializer):
    subscriber_email = serializers.EmailField(source="subscriber.email", read_only=True)

    class Meta:
        model = NewsletterSendLog
        fields = [
            "id",
            "campaign",
            "subscriber",
            "subscriber_email",
            "email_to",
            "status",
            "error",
            "created_at",
            "sent_at",
        ]
        read_only_fields = [
            "id",
            "status",
            "error",
            "created_at",
            "sent_at",
        ]


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = [
            "id",
            "language",
            "full_name",
            "email",
            "phone",
            "message",
            "is_sent",
            "sent_at",
            "error",
            "created_at",
        ]
        read_only_fields = ["id", "is_sent", "sent_at", "error", "created_at"]

    def validate_language(self, value: str) -> str:
        value = value.lower().strip()
        valid = {choice[0] for choice in ContactMessage.LANGUAGE_CHOICES}
        if value not in valid:
            raise serializers.ValidationError(f"language must be one of: {sorted(valid)}")
        return value


class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = [
            "id",
            "language",
            "full_name",
            "email",
            "phone",
            "company",
            "request_type",
            "description",
            "is_sent",
            "sent_at",
            "error",
            "created_at",
        ]
        read_only_fields = ["id", "is_sent", "sent_at", "error", "created_at"]

    def validate_language(self, value: str) -> str:
        value = value.lower().strip()
        valid = {choice[0] for choice in ServiceRequest.LANGUAGE_CHOICES}
        if value not in valid:
            raise serializers.ValidationError(f"language must be one of: {sorted(valid)}")
        return value
