import datetime
from django.utils import timezone
from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegisterSerializer
# , UserLoginSerializer

# test django_eventstream
from django_eventstream import send_event

UserModel = get_user_model()

class RegisterAPIView(generics.CreateAPIView):
    queryset                    = UserModel.objects.all()
    serializer_class            = UserRegisterSerializer
    permission_classes          = [permissions.AllowAny]


class LoginAPIView(APIView):
    permission_classes          = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return Response({'detail': 'Error: this user is already authenticated'}, status=400)

        data = request.data
        username = data.get('username')  # retrieve username or email
        password = data.get('password')
        user = authenticate(username=username, password=password)
        queryset = UserModel.objects.filter(
                    Q(username__iexact=username) |
                    Q(email__iexact=username)
                    ).distinct()
        if queryset.count() == 1:
            user_object = queryset.first()
            if user_object.check_password(password):
                user = user_object
                refresh = RefreshToken.for_user(user)
                access_delta = refresh.access_token.lifetime
                refresh_delta = refresh.lifetime
                access_expires = ( timezone.now() + access_delta - datetime.timedelta(seconds=10) ).isoformat(timespec='seconds')
                refresh_expires = ( timezone.now() + refresh_delta - datetime.timedelta(seconds=60) ).isoformat(timespec='seconds')
                response = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'access_expires': access_expires,
                    'refresh_expires': refresh_expires,
                }
                return Response(response)
        else:
            return Response({'detail': 'Error: invalid credentials'}, status=401)


# class LoginAPIView(TokenObtainPairView):
#     serializer_class            = UserLoginSerializer
#     permission_classes          = [permissions.AllowAny]
