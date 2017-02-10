# Create your models here.
import uuid
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    profile = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    Level = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    pikud = models.TextField()

    def __str__(self):
        return self.title


class VideoCall(models.Model):
    status_field = ['pending approval', 'approved', 'completed']
    status = models.TextField(choices=status_field, default='pending approval')
    VC_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    request_time = models.DateTimeField(
        default=timezone.now()
    )
    starting_time = models.DateTimeField(
        default=timezone.now())
    participants = models.TextField()  # change this to many to one key
    # add more conversation properties

    def __str__(self):
        return self.VC_id
