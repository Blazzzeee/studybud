from django.forms import ModelForm
from .models import Room, Message
from django import forms
#   DEFINE YOUR FORMS HERE

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']

        widgets = {
                'body':forms.TextInput(attrs={'class':'message-input', 'type':'text', 'placeholder': 'Message ....' })
                }
