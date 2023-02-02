from rest_framework import serializers
from .models import Meeting
from apps.contacts.serializer import ContactSerializer
from apps.contacts.models import Contact

class MeetingSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = Meeting
        fields = '__all__'

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        meeting = Meeting.objects.create(**validated_data)
        self.update_contacts(meeting, contacts_data)
        return meeting

    def update(self, instance, validated_data):
        contacts_data = validated_data.get('contacts', [])
        instance = super().update(instance, validated_data)
        self.update_contacts(instance, contacts_data)
        return instance

    def update_contacts(self, meeting, contacts_data):
        existing_contacts = Contact.objects.filter(meeting=meeting)
        existing_contact_ids = set(c.id for c in existing_contacts)

        for contact_data in contacts_data:
            contact_id = contact_data.get('id')
            if contact_id:
                existing_contact_ids.discard(contact_id)
                Contact.objects.filter(id=contact_id).update(
                    first_name=contact_data.get('first_name'),
                    last_name=contact_data.get('last_name'),
                    email=contact_data.get('email'),
                    phone_number=contact_data.get('phone_number')
                )
            else:
                Contact.objects.create(
                    meeting=meeting,
                    first_name=contact_data.get('first_name'),
                    last_name=contact_data.get('last_name'),
                    email=contact_data.get('email'),
                    phone_number=contact_data.get('phone_number')
                )
