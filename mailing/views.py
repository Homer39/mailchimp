from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, UpdateView, DeleteView, CreateView

from mailing.forms import MailingMessageForm, MailingSettingsForm, ClientForm
from mailing.models import MailingSettings, Client, MailingMessage


def main(request):
    return render(request, 'mailing/main.html')


class ClientListView(ListView):
    model = Client
    template_name = 'mailing/clients.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')


class MailingSettingsListView(ListView):
    model = MailingSettings


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailingsettings_list')


class MailingSettingsUpdateView(UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailingsettings_list')


class MailingSettingsDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailingsettings')


class MailingMessageListView(ListView):
    model = MailingMessage
    template_name = 'mailing/messages.html'


class MailingMessageCreateView(CreateView):
    model = MailingMessage
    form_class = MailingMessageForm
    template_name = 'mailing/message_form.html'
    success_url = reverse_lazy('messages')


class MailingMessageUpdateView(UpdateView):
    model = MailingMessage
    form_class = MailingMessageForm
    template_name = 'mailing/message_form.html'
    success_url = reverse_lazy('messages')


class MailingMessageDeleteView(DeleteView):
    model = MailingMessage
    template_name = 'mailing/message_confirm_delete.html'
    success_url = reverse_lazy('messages')


class ContactsTemplateView(TemplateView):
    template_name = 'mailing/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

    def post(self, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            email = self.request.POST.get('email')
            message = self.request.POST.get('message')
            print(f'New message from {name}, {email}: {message}')
        return super().get_context_data(**kwargs)
