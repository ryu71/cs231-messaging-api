import datetime
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):

    # password            = serializers.CharField(style = {'input_type': 'password'}, write_only = True)
    password_verify     = serializers.CharField(style = {'input_type': 'password'}, write_only = True)
    token_response      = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password_verify',
            'token_response',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact = value)
        if qs.exists():
            raise serializers.ValidationError("Error: username aleady exists")
        return value

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact = value)
        if qs.exists():
            raise serializers.ValidationError("Error: email already exists")
        return value

    def validate(self, data):
        pw = data.get('password')
        pw_verify = data.pop('password_verify')
        if pw != pw_verify:
            raise serializers.ValidationError("Error: passwords do not match")
        return data

    def create(self, validated_data):
        user_obj = User(
                    username=validated_data.get('username'),
                    email=validated_data.get('email'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj

    def get_token_response(self, object):
        user = object
        refresh = RefreshToken.for_user(user)
        access_delta = refresh.access_token.lifetime
        refresh_delta = refresh.lifetime
        access_expires = ( timezone.now() + access_delta - datetime.timedelta(seconds=10) ).isoformat(timespec='seconds')
        refresh_expires = ( timezone.now() + refresh_delta - datetime.timedelta(seconds=60) ).isoformat(timespec='seconds')

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'access_expires': access_expires,
            'refresh_expires': refresh_expires,
        }

# class UserLoginSerializer(TokenObtainPairSerializer):
#
#     def validate(self, attrs):
#         access_delta = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
#         refresh_delta = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
#
#         data = super().validate(attrs)
#         data['username'] = self.user.username
#         data['access_expires'] = timezone.now() + access_delta - datetime.timedelta(seconds=10)
#         data['refresh_expires'] = timezone.now() + refresh_delta - datetime.timedelta(seconds=60)
#         return data
