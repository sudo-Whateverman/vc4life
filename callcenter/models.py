# Create your models here.
import uuid
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    levels_field = (
        ('major', 'רב סרן'),
        ('lieutenant colonel', 'סגן אלוף'),
        ('colonel', 'אלוף משנה'),
        ('brigadier general', 'תת אלוף'),
        ('lieutenant general', 'אלוף'),
        ('chief of general staff', 'רב אלוף'),
        ('VCTech', 'טכנאי מערכת'),
        ('special privilege', 'הרשאה מיוחדת')
    )
    pikudim = (
        ('North', 'צפון'),
        ('Center', 'מרכז'),
        ('South', 'דרום'),
        ('Homefront', 'העורף'),
        ('DeepOp', 'העומק')
    )
    levels_field_iter = tuple(levels_field)
    profile = models.OneToOneField('auth.User', unique=True)
    title = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    level = models.CharField(max_length=30, choices=levels_field_iter)
    created_date = models.DateTimeField(
        default=timezone.now)
    pikud = models.CharField(max_length=30, choices=pikudim)

    def __str__(self):
        return self.title


class VideoCall(models.Model):
    status_field = (
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
        ('C', 'Completed'),
    )
    status = models.CharField(choices=status_field, default='P', max_length=20)
    VC_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    request_time = models.DateTimeField(default=timezone.now)
    starting_time = models.DateTimeField(default=timezone.now)
    participants = models.ManyToManyField(Profile, default=None, related_name='participants')
    vc_head = models.ForeignKey(Profile, default=None, related_name='vc_head')  # use request.user to get currently logged user.
    # add more conversation properties

    def __str__(self):
        return str(self.VC_id)

class VCallcenter(models.Model):
    name_of_callcenter = models.CharField(max_length=60)
    capacity = models.IntegerField()
    current_videocalls = models.ManyToManyField(VideoCall)
    status_field = (
        ('NW', 'Not Working'),
        ('W', 'Working'),
        ('M', 'Maintenance'),
        ('R', 'Reserved'),
        ('DNR', 'Does Not Respond')
    )
    status = models.CharField(choices=status_field, max_length=30)
