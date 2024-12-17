from django.shortcuts import render,get_object_or_404,redirect,Http404 
from .models import Room, Message
from .forms import RoomForm, MessageForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

rooms = Room.objects.all()

def home(request):
    context = None

    context = {'rooms':rooms}
    return render(request, 'base/index.html', context)

def room(request, id):
    context = None
    room = get_object_or_404(Room, pk=id)
    form = MessageForm()
    messages = Message.objects.filter(room= room)
    context = {'rooms':rooms , 'room':room, 'form':form, 'RoomMessages': messages}
 
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.room = room

            message.save()
            print('LOG:  MessageForm submitted!')

        else:
            print('LOG: MessageForm could not be submitted')

    return render(request, 'base/room.html', context)


#User crud operations



@login_required(login_url='login')
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

@login_required(login_url='login')
def update_room(request, id):

    room = get_object_or_404(Room, pk=id)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('The user does not have sufficient permissions to view the page')

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




#User session management (logout, register, login)


def loginView(request):

    page = 'login'

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'The username and password combination is incorrect')


    return render(request, 'base/login_register.html', { 'page': page })


def logoutUser(request):

    logout(request)

    return redirect('home')

def registerPage(request):
    #page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

       # print(f'DEBUG LOG: Register data received: {request.POST}')
        if form.is_valid():
           user = form.save(commit=False)
           user.username = user.username.lower()
           user.save()
           login(request, user)

           return redirect('home')

        else:
            print(form.errors)
            messages.error(request, 'An error occurred during registration! \n Please try again')

    context = {'form' : form }
    return render(request, 'base/login_register.html', context)


# Messages Crud operaton

def delete_message(request, id):

    context = {}


    return render(request, 'base/delete_room.html', context)




#Recent activity page        
    #All members 


def recent_page(request, ):
    messages = Message.objects.all()

    context = {'RoomMessages': messages}
    return render(request, 'base/recent.html', context)

