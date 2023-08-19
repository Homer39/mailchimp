from django import forms

from mailing.models import MailingMessage


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingMessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingMessage
        fields = '__all__'
