from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication  import SessionAuthentication
from messageapp.models import Messages
from .serializers import MessageSerializer
# from rest_framework.generics import ListAPIView

# test django_eventstream
from django_eventstream import send_event

# class MessagesListSearchAPIView(APIView):
#
#     def get(self, request, format=None):
#         queryset = Messages.objects.all()
#         serialized_qs = MessageSerializer(queryset, many=True)
#         return Response(serialized_qs.data)

class MessagesAPIView(generics.ListAPIView):
    permission_classes      = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes  = [SessionAuthentication]
    serializer_class        = MessageSerializer
    # queryset              = Messages.objects.all()

    def get_queryset(self):
        request = self.request
        print("user:", request.user)
        queryset = Messages.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(message__icontains=query)

        # test django_eventstream:
        # send_event('test', 'message', {'text': 'hello_world'})

        return queryset

class MessagesCreateAPIView(generics.CreateAPIView):
    # permission_classes      = [permissions.IsAuthenticated]
    # authentication_classes  = [SessionAuthentication]
    serializer_class        = MessageSerializer
    queryset                = Messages.objects.all()

    def perform_create(self, serializer):
        send_event('main', 'message', {'text': 'new message posted'})
        serializer.save(user = self.request.user)




# The following views are not being used:

class MessagesDetailAPIView(generics.RetrieveAPIView):
    # permission_classes      = []
    # authentication_classes  = []
    serializer_class        = MessageSerializer
    queryset                = Messages.objects.all()
    lookup_field            = 'id'  # or slug field

    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Messages.objects.get(id=kw_id)

class MessagesUpdateAPIView(generics.UpdateAPIView):
    # permission_classes      = []
    # authentication_classes  = []
    serializer_class        = MessageSerializer
    queryset                = Messages.objects.all()
    lookup_field            = 'id'

class MessagesDeleteAPIView(generics.DestroyAPIView):
    # permission_classes      = []
    # authentication_classes  = []
    serializer_class        = MessageSerializer
    queryset                = Messages.objects.all()
    lookup_field            = 'id'
