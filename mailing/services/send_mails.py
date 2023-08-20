import datetime

from smtplib import SMTPException
from django.conf import settings
from django.core.mail import send_mail

from mailing.models import MailingSettings, MailingLog


def _send_email(message_settings, message_client):
    result_txt = ('Усешно отправлена')
    try:
        result = send_mail(
            subject=message_settings.message.letter_subject,
            message=message_settings.message.letter_body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[message_client.client.email],
            fail_silently=False
        )

    except SMTPException as fail:
        result_txt = fail

    MailingLog.objects.create(
        try_status=MailingLog.STATUS_OK if result else MailingLog.STATUS_FAILED,
        mailing=message_settings,
        client_id=message_client.client_id,
        mailing_service_response=result_txt
    )


def send_mails():
    datetime_now = datetime.datetime.now(datetime.timezone.utc)
    for mailing_setting in MailingSettings.objects.filter(status=MailingSettings.STATUS_STARTED):

        if (datetime_now > mailing_setting.start_time) and (datetime_now < mailing_setting.end_time):

            for mailing_client in mailing_setting.mailingclient_set.all():

                mailing_log = MailingLog.objects.filter(
                    client=mailing_client.client,
                    mailing=mailing_setting
                )

                if mailing_log.exists():
                    last_try_date = mailing_log.order_by('-last_attempt').first().last_attempt

                    if mailing_setting.period == MailingSettings.PERIOD_DAILY:
                        if (datetime_now - last_try_date).days >= 1:
                            _send_email(mailing_setting, mailing_client)
                    elif mailing_setting.period == MailingSettings.PERIOD_WEEKLY:
                        if (datetime_now - last_try_date).days >= 7:
                            _send_email(mailing_setting, mailing_client)
                    elif mailing_setting.period == MailingSettings.PERIOD_MONTHLY:
                        if (datetime_now - last_try_date).days >= 30:
                            _send_email(mailing_setting, mailing_client)

                else:
                    _send_email(mailing_setting, mailing_client)
