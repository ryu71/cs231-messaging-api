from django.conf.urls import url
from .views import  (
                        MessagesAPIView,
                        MessagesCreateAPIView,
                        MessagesDetailAPIView,
                        MessagesUpdateAPIView,
                        MessagesDeleteAPIView,
                    )

from .token_views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    url(r'^$', MessagesAPIView.as_view()),
    url(r'^create/$', MessagesCreateAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', MessagesDetailAPIView.as_view()),
    url(r'^(?P<id>\d+)/update/$', MessagesUpdateAPIView.as_view()),
    url(r'^(?P<id>\d+)/delete/$', MessagesDeleteAPIView.as_view()),

    url(r'^token/$', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='toke_refresh'),
]

# /api/messageapp/              -> List & Search
# /api/messageapp/create/       -> Create
# /api/messageapp/##/           -> Detail
# /api/messageapp/##/update     -> Update
# /api/messageapp/##/delete     -> Delete
