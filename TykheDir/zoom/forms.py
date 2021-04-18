from django.forms import ModelForm
from django import forms
from .models import ZoomMtg

class TimeInput(forms.TimeInput):
    input_type='time'

class ZForm(ModelForm):
    class Meta:
        widgets = {
            'time': TimeInput(attrs={'class': 'form-control'}),
            'ZoomUrl': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
        model=ZoomMtg
        fields = ['title', 'ZoomUrl', 'time']
