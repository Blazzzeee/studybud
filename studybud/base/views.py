from django.shortcuts import render,get_object_or_404,redirect,Http404
from .models import Room
from .forms import RoomForm
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

def create_room(request):
    context = None

    if request.method =='POST':
        form = RoomForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return Http404('ERROR SUBMITTING FORM , FORM INVALID!!!')

    else: 
        form = RoomForm()
        context = {'form': form}
        return render(request, 'base/room_form.html', context)


def update_room(request, id):
    
    room = get_object_or_404(Room, pk=id)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}

    return render (request, 'base/room_form.html', context)


def delete_room(request, id):
    form = get_object_or_404(Room, pk=id)
    if request.method == 'POST':
        form.delete()
        print(f'LOG: Database entry deleted with {id}')
        return redirect('home')

    context = {'room':room}
    return render(request, 'base/room_delete.html', context)