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
