from mailing.apps import MailingConfig
from django.urls import path

from mailing.views import main, MailingSettingsListView, ClientListView, MailingMessageListView, ContactsTemplateView, \
    MailingMessageUpdateView, MailingMessageDeleteView, MailingSettingsUpdateView, MailingSettingsCreateView, \
    MailingSettingsDeleteView, MailingMessageCreateView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('', main, name='main'),

    path('settings/', MailingSettingsListView.as_view(), name='mailingsettings_list'),
    path('settings/create_settings/', MailingSettingsCreateView.as_view(), name='settings_create'),
    path('settings/edit_settings/<int:pk>/', MailingSettingsUpdateView.as_view(), name='settings_edit'),
    path('settings/delete_settings/<int:pk>/', MailingSettingsDeleteView.as_view(), name='settings_delete'),

    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/create/', ClientCreateView.as_view(), name='create_client'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    path('messages/', MailingMessageListView.as_view(), name='messages'),
    path('messages/create_messages', MailingMessageCreateView.as_view(), name='create_message'),
    path('messages/edit_message/<int:pk>/', MailingMessageUpdateView.as_view(), name='update_message'),
    path('messages/delete_message/<int:pk>/', MailingMessageDeleteView.as_view(), name='delete_message'),

    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
]
