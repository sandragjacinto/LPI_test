from rest_framework import serializers
from .models import Meeting
from apps.contacts.serializer import ContactSerializer

class MeetingSerializer(serializers.ModelSerializer):
    contacts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Meeting
        fields = ['title','description','date','duration','contacts','status']
