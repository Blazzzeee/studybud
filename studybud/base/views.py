from django.shortcuts import render,get_object_or_404
from .models import Room
# Create your views here.


rooms = Room.objects.all()

def home(request):
    context = None
    
    context = {'rooms':rooms}
    return render(request, 'base/index.html', context)

def room(request, id):
    context = None
    room = get_object_or_404(Room, pk=id)
    context = {'rooms':rooms , 'room':room}
    return render(request, 'base/room.html', context)

