from __future__ import annotations

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.db import transaction
from django.utils import timezone

from .models import ContactMessage, NewsletterCampaign, NewsletterSendLog, NewsletterSubscriber, ServiceRequest


@shared_task(bind=True)
def send_newsletter_campaign(self, campaign_id: int) -> str:
    campaign = NewsletterCampaign.objects.select_for_update().get(id=campaign_id)

    now = timezone.now()
    if campaign.status not in {NewsletterCampaign.STATUS_SCHEDULED, NewsletterCampaign.STATUS_RUNNING}:
        return f"skip: campaign status={campaign.status}"

    campaign.status = NewsletterCampaign.STATUS_RUNNING
    campaign.save(update_fields=["status"])

    from_email = settings.DEFAULT_FROM_EMAIL
    sender_name = getattr(settings, "NEWSLETTER_SENDER_NAME", "")

    subscribers = NewsletterSubscriber.objects.filter(
        is_active=True,
        language=campaign.language,
    ).only("id", "email")

    created_logs = 0
    for subscriber in subscribers:
        if NewsletterSendLog.objects.filter(campaign=campaign, email_to=subscriber.email).exists():
            continue

        email_to = subscriber.email
        try:
            with transaction.atomic():
                log = NewsletterSendLog.objects.create(
                    campaign=campaign,
                    subscriber_id=subscriber.id,
                    email_to=email_to,
                    status=NewsletterSendLog.STATUS_QUEUED,
                    error="",
                )

                send_mail(
                    subject=campaign.subject,
                    message=campaign.body,
                    from_email=f"{sender_name} <{from_email}>" if sender_name else from_email,
                    recipient_list=[email_to],
                    fail_silently=False,
                )

                log.status = NewsletterSendLog.STATUS_SENT
                log.sent_at = timezone.now()
                log.error = ""
                log.save(update_fields=["status", "sent_at", "error"])

                created_logs += 1
        except Exception as exc:  # noqa: BLE001
            NewsletterSendLog.objects.create(
                campaign=campaign,
                subscriber_id=subscriber.id,
                email_to=email_to,
                status=NewsletterSendLog.STATUS_FAILED,
                error=str(exc),
            )

    campaign.status = NewsletterCampaign.STATUS_SENT
    campaign.sent_at = now
    campaign.save(update_fields=["status", "sent_at"])

    return f"ok: campaign_id={campaign_id}, new_logs={created_logs}"


@shared_task
def send_due_newsletters() -> int:
    now = timezone.now()

    due_campaigns = NewsletterCampaign.objects.filter(
        status=NewsletterCampaign.STATUS_SCHEDULED,
        scheduled_at__lte=now,
    ).only("id", "status", "scheduled_at")

    for campaign in due_campaigns:
        send_newsletter_campaign.delay(campaign.id)

    return due_campaigns.count()


@shared_task
def send_contact_message(message_id: int) -> None:
    msg = ContactMessage.objects.get(id=message_id)
    if msg.is_sent:
        return

    nce_recipient = (
        getattr(settings, "CONTACT_RECIPIENT_EMAIL", None)
        or getattr(settings, "SERVICE_RECIPIENT_EMAIL", None)
        or getattr(settings, "DEFAULT_FROM_EMAIL", None)
        or "noreply@example.com"
    )

    client_recipient = msg.email

    nce_phone_fr = getattr(settings, "NCE_PHONE_FR", "") or "+33 749224279"
    nce_phone_cm = getattr(settings, "NCE_PHONE_CM", "") or "+237 656728560"
    nce_email = getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@example.com")

    nce_subject_fr = "Nouveau message de contact"
    nce_subject_en = "New contact message"

    client_subject_fr = "Merci pour votre demande — NCE Outsourcing"
    client_subject_en = "Thank you for your request — NCE Outsourcing"

    nce_subject = nce_subject_fr if msg.language == ContactMessage.LANGUAGE_FR else nce_subject_en
    client_subject = client_subject_fr if msg.language == ContactMessage.LANGUAGE_FR else client_subject_en

    client_text = (
        "NCE Outsourcing — Confirmation de votre demande\n"
        "------------------------------------------------\n"
        "Bonjour,\n"
        "\n"
        "Merci de nous avoir contactés. Nous avons bien reçu votre demande et nous vous répondrons dans les meilleurs délais.\n"
        "\n"
        "Nous vous proposons des solutions sur mesure pour votre entreprise (selon vos besoins : appels/outsourcing/gestion de la relation client).\n"
        "\n"
        "Détails de votre demande:\n"
        f"- Nom: {msg.full_name}\n"
        f"- Email: {msg.email}\n"
        f"- Téléphone: {msg.phone or '-'}\n"
        "\n"
        "Message:\n"
        f"{msg.message}\n"
        "\n"
        "------------------------------------------------\n"
        "English\n"
        "------------------------------------------------\n"
        "Hello,\n"
        "\n"
        "Thank you for reaching out. We have received your request and will get back to you as soon as possible.\n"
        "\n"
        "We offer tailored solutions for your business based on your needs (calls/outsourcing/customer relationship management).\n"
        "\n"
        "Your request details:\n"
        f"- Name: {msg.full_name}\n"
        f"- Email: {msg.email}\n"
        f"- Phone: {msg.phone or '-'}\n"
        "\n"
        "Message:\n"
        f"{msg.message}\n"
        "\n"
        "------------------------------------------------\n"
        "Sincerely,\n"
        "NCE Outsourcing\n"
    )

    nce_text = (
        "NCE Outsourcing — Nouveau message de contact\n"
        "------------------------------------------------\n"
        f"Nom: {msg.full_name}\n"
        f"Email: {msg.email}\n"
        f"Téléphone: {msg.phone or '-'}\n\n"
        f"Message:\n{msg.message}\n\n"
        "------------------------------------------------\n"
    )

    from_email = getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@example.com")

    try:
        send_mail(
            subject=client_subject,
            message=client_text,
            from_email=from_email,
            recipient_list=[client_recipient],
            fail_silently=False,
        )

        send_mail(
            subject=nce_subject,
            message=nce_text,
            from_email=from_email,
            recipient_list=[nce_recipient],
            fail_silently=False,
        )

        msg.is_sent = True
        msg.sent_at = timezone.now()

        client_preview = client_text[:500].replace("\n", "\\n")
        nce_preview = nce_text[:300].replace("\n", "\\n")
        msg.error = (
            f"sent_to={client_recipient}, {nce_recipient}; "
            f"client_preview={client_preview}; nce_preview={nce_preview}"
        )
        msg.save(update_fields=["is_sent", "sent_at", "error"])
    except Exception as exc:  # noqa: BLE001
        msg.is_sent = False
        msg.error = str(exc)
        msg.save(update_fields=["is_sent", "error"])


@shared_task
def send_service_request(request_id: int) -> None:
    req = ServiceRequest.objects.get(id=request_id)
    if req.is_sent:
        return

    recipient = req.email

    subject_fr = "Nouvelle demande de service"
    subject_en = "New service request"
    subject = subject_fr if req.language == ServiceRequest.LANGUAGE_FR else subject_en

    phone_part = req.phone or "-"

    nce_phone_fr = (getattr(settings, "NCE_PHONE_FR", "") or "+33 749224279")
    nce_phone_cm = (getattr(settings, "NCE_PHONE_CM", "") or "+237 656728560")
    nce_email = getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@example.com")

    text = (
        "NCE Outsourcing — Nouvelle demande de service\n"
        "================================================\n\n"
        "Infos client\n"
        "-------------\n"
        f"Nom: {req.full_name}\n"
        f"Email: {req.email}\n"
        f"Téléphone: {phone_part}\n"
        f"Société: {req.company or '-'}\n"
        f"Type de demande: {req.request_type or '-'}\n\n"
        "Message\n"
        "-------\n"
        f"{req.description}\n\n"
        "------------------------------------------------\n"
        "Contact NCE Outsourcing\n"
        f"- Téléphone (FR): {nce_phone_fr or '-'}\n"
        f"- Téléphone (CM): {nce_phone_cm or '-'}\n"
        f"- Email: {nce_email}\n"
        "\nCordialement,\nNCE Outsourcing\n"
    )

    try:
        send_mail(
            subject=subject,
            message=text,
            from_email=getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@example.com"),
            recipient_list=[recipient],
            fail_silently=False,
        )
        req.is_sent = True
        req.sent_at = timezone.now()
        req.error = ""
        req.save(update_fields=["is_sent", "sent_at", "error"])
    except Exception as exc:  # noqa: BLE001
        req.is_sent = False
        req.error = str(exc)
        req.save(update_fields=["is_sent", "error"])
