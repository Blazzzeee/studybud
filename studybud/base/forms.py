from django.forms import ModelForm
from .models import Room
#   DEFINE YOUR FORMS HERE

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
     
