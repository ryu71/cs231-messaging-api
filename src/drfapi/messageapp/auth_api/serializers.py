from rest_framework import serializers
from messageapp.models import Messages

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = [
            'id',
            'user',
            'email',
            'message',
            # 'content',
            # 'image'
        ]
        read_only_fields = ['user']  # can read using GET requests

    def validate_message(self, value):
        if len(value) > 256:
            raise serializers.ValidationError('Error: message is too long')
        return value

    # def validate(self, data):
    #     message = data.get('message', None)
    #     content = data.get('content', None)
    #     if message == '':
    #         message = None
    #     if content == '':
    #         content = None
    #     if message is None and content is None:
    #         raise serializers.ValidationError('Error: either message or content is required')
    #     return data
