# Create your views here.
from apps.contacts.models import Contact
from apps.contacts.serializer import ContactSerializer
from .models import Meeting
from .serializer import MeetingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import exceptions, generics, status

#CRUD
class MeetingsList(generics.ListAPIView):
    serializer_class = MeetingSerializer

    def get_queryset(self):
        queryset = Meeting.objects.all()
        meeting_status = self.request.query_params.get('status')
        if meeting_status is not None:
            queryset = queryset.filter(status=meeting_status)
        return queryset

class MeetingCreateView(generics.CreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def perform_create(self, serializer):
        meeting = serializer.save()
        contacts = self.request.data.get('contacts', [])
        for contact_data in contacts:
            obj, created = Contact.objects.get_or_create(email=contact_data.get('email'), id=contact_data.get('id'))
            meeting.contacts.add(obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MeetingDetailView(generics.RetrieveAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    lookup_field = 'id'

class MeetingUpdateView(generics.UpdateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def perform_update(self, serializer):
        meeting = self.get_object()
        serializer.save()
        meeting.contacts.clear()
        contacts = self.request.data.get('contacts', [])
        for contact_data in contacts:
            obj, created = Contact.objects.get_or_create(email=contact_data.get('email'), id=contact_data.get('id'))
            meeting.contacts.add(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MeetingDeleteView(generics.DestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
