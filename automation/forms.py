from django import forms
from .models import AddUser, EmailGroup

class SendEmailForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ('Subject')}))
    message = forms.CharField(widget=forms.Textarea)
    Group = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ('Group')}))
