from django.contrib import admin
import callcenter
# Register your models here.
admin.site.register(callcenter.models.VideoCall)
admin.site.register(callcenter.models.Profile)
admin.site.register(callcenter.models.VCallcenter)
