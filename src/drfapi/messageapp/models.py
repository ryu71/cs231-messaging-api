from django.conf import settings
from django.db import models

def upload_messages_image(instance, filename):
    return 'messages/{user}/{filename}'.format(user=instance.user, filename=filename)

class MessagesQuerySet(models.QuerySet):
    pass

class MessagesManager(models.Manager):
    def get_queryset(self):
        return MessagesQuerySet(self.model, using=self._db)

# Primary Messages Model
class Messages(models.Model):  # instant messages
    #id             = models.AutoField(primary_key=True)
    user            = models.ForeignKey(settings.AUTH_USER_MODEL)
    email           = models.EmailField()
    message         = models.TextField(null=True, blank=True)
    content         = models.TextField(null=True, blank=True)
    image           = models.ImageField(upload_to=upload_messages_image, null=True, blank=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now_add=True)

    objects         = MessagesManager()

    def __str__(self):
        return str(self.message)[:128]

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
