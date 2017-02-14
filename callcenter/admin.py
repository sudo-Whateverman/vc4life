from django.contrib import admin
import callcenter
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Location
from mptt.admin import MPTTModelAdmin

admin.site.register(callcenter.models.VideoCall)
admin.site.register(callcenter.models.Profile)
admin.site.register(callcenter.models.VCallcenter)
admin.site.register(callcenter.models.VCkit)
admin.site.register(Location, MPTTModelAdmin)
#admin.site.register(callcenter.models.ApiUse)



class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)