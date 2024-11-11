from django.contrib import admin
from ownsite.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email_address', 'subject', 'message', 'created_at', 'is_published')  # message qo'shildi
    list_filter = ('is_published', 'created_at')
    search_fields = ('full_name', 'email_address', 'subject')
