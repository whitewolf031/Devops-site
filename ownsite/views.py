from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from ownsite.models import Contact
from ownsite.serializator import ContactSerializer


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]  # Har qanday foydalanuvchi yuborishi mumkin

class DevopsRetrive(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAdminUser,)

class DevopsDestroy(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAdminUser,)