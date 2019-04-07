from django.conf.urls import url
from .views import  (
                        MessagesAPIView,
                        MessagesCreateAPIView,
                        MessagesDetailAPIView,
                        MessagesUpdateAPIView,
                        MessagesDeleteAPIView,
                    )

urlpatterns = [
    url(r'^$', MessagesAPIView.as_view()),
    url(r'^create/$', MessagesCreateAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', MessagesDetailAPIView.as_view()),
    url(r'^(?P<id>\d+)/update/$', MessagesUpdateAPIView.as_view()),
    url(r'^(?P<id>\d+)/delete/$', MessagesDeleteAPIView.as_view()),
]

# /api/messageapp/              -> List & Search
# /api/messageapp/create/       -> Create
# /api/messageapp/##/           -> Detail
# /api/messageapp/##/update     -> Update
# /api/messageapp/##/delete     -> Delete
