from django.forms import ModelForm
from django import forms
from .models import Todo


class DateInput(forms.DateInput):
    input_type='date'

class TodoForm(ModelForm):
    class Meta:
        widgets={'due': DateInput(attrs={'class': 'form-control'}),
                 'url': forms.URLInput(attrs={'class': 'form-control'}),
                 'name': forms.TextInput(attrs={'class': 'form-control'}),
                 'important': forms.CheckboxInput(attrs={'class': 'form-check-label'})
                 }
        model=Todo
        fields=['name', 'url', 'due', 'important']