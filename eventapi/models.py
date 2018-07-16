from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.core.validators import MinValueValidator


class UserInfo(models.Model):

    RSVP_RESPONSE_CHOICES = (
        ('YES', 'Yes'),
        ('NO', 'No'),
        ('NO_RESPONSE', 'No Response'),
    )

    address = models.CharField(max_length=64)
    phone_nubmer = models.CharField(max_length=21)
    rsvp_status = models.CharField(max_length=11, choices=RSVP_RESPONSE_CHOICES)
    party_size = models.PositiveIntegerField(validators=[MinValueValidator(1)])


class Message(models.Model):
    from_user = models.ForeignKey(User, related_name='message_from', on_delete=models.PROTECT)
    to_user = models.ForeignKey(User, related_name='message_to', on_delete=models.PROTECT)
    content = models.TextField()
    viewed = models.BooleanField(default=False)


class Announcement(models.Model):
    created = models.DateField(auto_now=True)
    due_date = models.DateField(null=True)
    title = models.CharField(max_length=120, null=True)
    content = models.TextField()
    url = models.CharField(max_length=120, null=True)

    def __str__(self):
        return '{0}'.format(self.title)


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateField(auto_now=True)
    due_date = models.DateField(null=True)
    content = models.TextField()
    complete = models.BooleanField(default=False)

class KauaiSuggestion(models.Model):
    created = models.DateField(auto_now=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    url = models.CharField(max_length=120, null=True)
