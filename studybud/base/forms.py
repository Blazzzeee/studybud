from django.forms import ModelForm
from .models import Room, Message, User
from django import forms
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
    email = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Email',
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
        fields = ['email', 'password1', 'password2', 'name', 'avatar']
        widgets = {
            'email': forms.TextInput(attrs={
                'placeholder': 'Email',
                'autocomplete': 'off',
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Username', 
                'autocomplete': 'off'
                })
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['name']  # Explicitly set the username field

        if commit:
            user.save()
        return user

   
