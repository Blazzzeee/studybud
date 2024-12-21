from django.forms import ModelForm
from .models import Room, Message
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#   DEFINE YOUR FORMS HERE

class RoomForm(ModelForm):
    class Meta:
        model = Room
        exclude = ['host']
        widgets = {
                'description':forms.Textarea(attrs={'cols': 18, 'rows': 5}),
                }



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
      

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username',
                'autocomplete': 'off',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Update placeholders and add help text
        self.fields['username'].help_text = (
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        )
        self.fields['password1'].help_text = (
            "Your password can’t be too similar to your other personal information.<br>"
            "Your password must contain at least 8 characters.<br>"
            "Your password can’t be a commonly used password.<br>"
            "Your password can’t be entirely numeric."
        )
        self.fields['password2'].help_text = "Enter the same password as above, for verification."
        
        # Set placeholder for password fields
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password',
            'autocomplete': 'off',
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm Password',
            'autocomplete': 'off',
        })


