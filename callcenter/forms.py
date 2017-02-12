from datetimewidget.widgets import DateTimeWidget

__author__ = 'nick'
from django import forms
from .models import Profile, VideoCall


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('title', 'name', 'pikud', 'level')


class VCallForm(forms.ModelForm):

    class Meta:
        model = VideoCall
        fields = ('starting_time', 'participants')
        widgets ={
            'starting_time': DateTimeWidget(bootstrap_version=3)}

    def __init__ (self, *args, **kwargs):
        super(VCallForm, self).__init__(*args, **kwargs)
        self.fields["participants"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["participants"].help_text = "The people you want to talk to"
        self.fields["participants"].queryset = Profile.objects.all()  # TODO: here we need to add our  fancy filter