from django.db import models

from realpal.apps.users.models import User


def message_attachment(instance, filename):
    return '{room}/files/{user}/{file}'.format(room=instance.room_id, user=instance.sent_by.id, file=filename)


class Room(models.Model):
    client = models.OneToOneField(User, related_name='Client',  on_delete=models.CASCADE)
    agent = models.ForeignKey(User, related_name='Agent', blank=True, null=True)

    def __str__(self):
        return '{owner} room'.format(owner=self.client.username)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='room', db_index=True)
    sent_by = models.ForeignKey(User, related_name='sender')
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
    attachment = models.FileField(upload_to=message_attachment, blank=True, null=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return 'sender: {sender}'.format(
            sender=self.sent_by.name,
        )
