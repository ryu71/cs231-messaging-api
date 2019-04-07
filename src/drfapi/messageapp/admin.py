from django.contrib import admin
from .models import Messages
from .forms import MessagesForm

class MessagesAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'email',
        'message',
        'content',
        'image']
    form = MessagesForm
    class Meta:
        model = Messages

admin.site.register(Messages, MessagesAdmin)
