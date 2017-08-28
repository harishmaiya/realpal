from django.contrib import admin

# Register your models here.
from realpal.apps.chat.models import Room, Message


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('client', 'agent', 'id')
    list_filter = ('agent',)
    search_fields = ('client', 'agent')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'sent_by', 'text', 'timestamp', 'attachment')
    list_filter = ('sent_by',)
    search_fields = ('sent_by', 'text')
