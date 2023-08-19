from django.contrib import admin

from mailing.models import Client, MailingSettings, MailingMessage, MailingLog, MailingClient


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('last_name',)


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'period', 'status', 'message')
    list_filter = ('status',)


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('letter_subject', 'letter_body')


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('last_attempt', 'try_status', 'mailing_service_response', 'mailing')
    list_filter = ('try_status',)


@admin.register(MailingClient)
class MailingClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'mailing', 'client')
    list_filter = ('client',)
