from django.contrib.auth.models import User
from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)  # Admin tomonidan ko'rinadigan yoki yo'qligi
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Foydalanuvchi

    def __str__(self):
        return f"Message from {self.full_name}"
