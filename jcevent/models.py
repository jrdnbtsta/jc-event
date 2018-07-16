from django.db import models
from django.contrib.auth.models import User, Group, Permission

class UserInfo(models.Model):

    RSVP_RESPONSE_CHOICES = (
        ('YES', 'Yes'),
        ('NO', 'No'),
        ('NO_RESPONSE', 'No Response'),
    )

    address = models.CharField(max_length=64)
    phone_nubmer = models.CharField(max_length=21)
    rsvp_status = models.CharField(max_length=11, choices=RSVP_RESPONSE_CHOICES)
    party_size = models.IntegerField(min=1)


class Messsage(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.SET_NULL)
    to_user = models.ForeignKey(User, on_delete=models.SET_NULL)
    content = models.CharField(max_length=240)
    viewed = models.BooleanField(default=False)


class Announcements(models.Model):
    created = models.DateField(auto_now=True)
    due_date = models.DateField(null=True)
    content = models.CharField(max_length=240)
    url = models.CharField(max_length=120, null=True)
