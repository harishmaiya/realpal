from django.db import models

from realpal.users.models import User


def message_attachment(instance, filename):
    return '{id}/messages/attachments/{filename}'.format(id=instance.sent_by.id, filename=filename)


class Room(models.Model):
    client = models.ForeignKey(User, related_name='Client',  on_delete=models.CASCADE)
    agent = models.ForeignKey(User, related_name='Agent', blank=True, null=True)

    def __str__(self):
        return '{owner} room'.format(owner=self.client.username)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='room', db_index=True)
    sent_by = models.ForeignKey(User, related_name='sender')
    text = models.TextField()
    attachment = models.FileField(upload_to=message_attachment, blank=True, null=True)

    def __str__(self):
        return '{timestamp}: sender: {sender}'.format(
            timestamp=self.formatted_timestamp,
            sender=self.sent_by.name,
        )
