from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parser import JSONParser

from messageapp.api.serializers import MessageSerializer
from messageapp.models import Messages

# Serialize a single object
object = Messages.objects.first()
serialized_object = MessageSerializer(serialized_object)
serialized_object.data
json_data = JSONRenderer().render(serialized_object.data)
json_data

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
data

# Serialize a queryset
queryset = Messages.objects.all()
serialized_qs = MessageSerializer(queryset, many=True)
serialized_qs.data
json_data = JSONRenderer().render(serialized_qs.data)
json_data

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
data

# Create object
data = {'user': 1, 'email': 'ryu71@mail.ccsf.edu'}
serialized_object = MessageSerializer(data=data)
if serialized_object.is_valid():
    serialized_object.save()

# Update object
object_id = 3
queryset = Messages.objects.all()
update_object = queryset[object_id-1]
data = {
    'user': 1,
    'email': 'ryu71@mail.ccsf.edu',
    'message': 'updated message1'
}
serialized_update_object = MessageSerializer(update_object, data=data)
if serialized_update_object.is_valid():
    serialized_update_object.save()

# Delete object (create a new object first)
data = {'user': 1, 'email': 'ryu71@mail.ccsf.edu', 'message': 'new message to be deleted'}
serialized_object = MessageSerializer(data=data)
serialized_object.is_valid()
returned_object = serialized_object.save()  # returns an instance of the object
returned_object

# Retrieve the most recently created object, and delete
recent_object = Messages.objects.last()
print(recent_object.delete())
