# Create your models here.
import uuid
from django.db import models
from django.utils import timezone
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Location(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class VCkit(models.Model):
    name_of_kit = models.CharField(max_length=30)
    ip = models.GenericIPAddressField(unique=True)
    pikudim = (
        ('North', 'צפון'),
        ('Center', 'מרכז'),
        ('South', 'דרום'),
        ('Homefront', 'העורף'),
        ('DeepOp', 'העומק')
    )
    pikud = models.CharField(max_length=30, choices=pikudim)
    location = models.ForeignKey(Location, blank=True, null=True,)

    def __str__(self):
        return self.ip

class Profile(models.Model):
    pikudim = (
        ('North', 'צפון'),
        ('Center', 'מרכז'),
        ('South', 'דרום'),
        ('Homefront', 'העורף'),
        ('DeepOp', 'העומק')
    )
    pikud = models.CharField(max_length=30, choices=pikudim)
    profile = models.OneToOneField('auth.User', unique=True)
    title = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    id_number = models.CharField(max_length=20, unique=True, default='1')
    created_date = models.DateTimeField(
        default=timezone.now)
    vckits = models.ManyToManyField(VCkit, blank=True)
    location = models.ForeignKey(Location, blank=True, null=True,)

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
    VC_id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, max_length=10)
    request_time = models.DateTimeField(default=timezone.now)
    starting_time = models.DateTimeField(default=timezone.now)
    ending_time = models.DateTimeField(default=timezone.now)
    participants = models.ManyToManyField(VCkit, default=None, related_name='participants')
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


class ApiUse(models.Model):
    MCU_ip = models.GenericIPAddressField()
    DMA_ip = models.GenericIPAddressField()
    RM_ip = models.GenericIPAddressField()

class Rmxrules(models.Model):
    matkal = models.IntegerField()
    tzameret_a = models.IntegerField()
    tzameret_a_redundant = models.IntegerField()
    tzameret_b = models.IntegerField()

class VCversion(models.Model):
    VSX_version = models.CharField(max_length=100)
    HDX_version = models.CharField(max_length=100)
    GROUP_version = models.CharField(max_length=100)

