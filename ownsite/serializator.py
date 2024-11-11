from rest_framework import serializers
from ownsite.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['full_name', 'email_address', 'phone_number', 'subject', 'message', 'user']
        read_only_fields = ['user']  # Foydalanuvchi maydoni o'qish uchun
