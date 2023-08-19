from mailing.apps import MailingConfig
from django.urls import path

from mailing.views import main, MailingSettingsListView, ClientListView, MailingMessageListView, ContactsTemplateView, \
    MailingMessageUpdateView, MailingMessageDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('', main, name='main'),

    path('mailing/', MailingSettingsListView.as_view(), name='mailingsettings_list'),

    path('clients/', ClientListView.as_view(), name='clients'),

    path('messages/', MailingMessageListView.as_view(), name='messages'),
    path('edit_message/<int:pk>/', MailingMessageUpdateView.as_view(), name='update_message'),
    path('delete_message/<int:pk>/', MailingMessageDeleteView.as_view(), name='delete_message'),

    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
]


