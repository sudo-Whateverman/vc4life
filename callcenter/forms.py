from datetimewidget.widgets import DateTimeWidget

__author__ = 'nick'
from django import forms
from .models import Profile, VideoCall, VCkit, ApiUse, VCversion, Rmxrules, Location
import django_tables2 as tables

class SimpleTableVideo(tables.Table):
    class Meta:
        model = VideoCall

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('title', 'name', 'id_number')


class VCallForm(forms.ModelForm):

    class Meta:
        model = VideoCall
        dateTimeOptions = {
            'format': '%Y-%m-%d %H:%M:%S',
        }
        fields = (
            'starting_time',
            'ending_time',
            'participants',
            )
        widgets ={
            'starting_time': DateTimeWidget(bootstrap_version=2, usel10n=True),
            'ending_time': DateTimeWidget(bootstrap_version=2, usel10n=True),
        }

    def __init__(self, pikud_form=None, location_form=None, *args, **kwargs):
        super(VCallForm, self).__init__(*args, **kwargs)
        self.locations = Location.objects.get(name=location_form).get_descendants(include_self=False)
        self.fields["participants"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["participants"].help_text = "The people you want to talk to"
        self.kits = VCkit.objects.filter(pikud=pikud_form, location=location_form)
        for lo in self.locations:
             self.kits = self.kits | VCkit.objects.filter(pikud=pikud_form, location=lo) # TODO: here we need to add our  fancy filter
        self.fields["participants"].queryset = self.kits

class ProfileKitForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('vckits',)

    def __init__(self, pikud_form=None, location_form=None, *args, **kwargs):
        super(ProfileKitForm, self).__init__(*args, **kwargs)
        self.fields["vckits"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["vckits"].help_text = "The kits that belong to you"
        self.fields["vckits"].queryset = VCkit.objects.filter(pikud=pikud_form)


class ApiUseForm(forms.ModelForm):

    class Meta:
        model = ApiUse
        fields = ('MCU_ip', 'DMA_ip', 'RM_ip')

class VersionForm(forms.ModelForm):

    class Meta:
        model = VCversion
        fields = ('VSX_version', 'HDX_version', 'GROUP_version')

class RmxrulesForms(forms.ModelForm):

    class Meta:
        model = Rmxrules
        fields = ('matkal', 'tzameret_a', 'tzameret_a_redundant', 'tzameret_b')



