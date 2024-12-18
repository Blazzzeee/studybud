from django.forms import ModelForm
from .models import Room, Message
from django import forms
from django.contrib.auth.models import User
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

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'id': 'username',
            'autocomplete': 'off',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'id': 'password',
            'autocomplete': 'off',
        })
    )
        
