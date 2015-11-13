from django import forms
from .models import Item

class PostForm(forms.Form):
    Task_Description = forms.CharField(max_length=256,required=False)
    completed = forms.BooleanField(required=False)

class getData(forms.Form):
    Edit_Task_Description = forms.CharField(max_length=256)