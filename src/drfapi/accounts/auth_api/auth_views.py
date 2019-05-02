# import datetime
# from django.utils import timezone
# from django.conf import settings
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
#
# access_delta = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
# refresh_delta = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
#
# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         data['username'] = self.user.username
#         data['access_expires'] = timezone.now() + access_delta - datetime.timedelta(seconds=10)
#         data['refresh_expires'] = timezone.now() + refresh_delta - datetime.timedelta(seconds=60)
#         return data
#
# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer
