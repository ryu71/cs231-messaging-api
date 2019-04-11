from django import forms
from .models import Messages

class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = [
            # 'user',
            'email',
            'message',
            'content',
            'image'
        ]

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        message = data.get('message', None)
        content = data.get('content', None)
        if message == '':
            message = None
        if content == '':
            content = None
        if message is None and content is None:
            raise forms.ValidationError('Error: either message or content is required')
        return super().clean(*args, **kwargs)

    def clean_message(self, *args, **kwargs):
        message = self.cleaned_data.get('message', None)
        if len(message) > 256:
            raise forms.ValidationError('Error: message is too verbose')
        return message
