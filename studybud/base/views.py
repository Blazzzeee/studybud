from django.shortcuts import render,get_object_or_404,redirect,Http404
from .models import Room, Message
from .forms import RoomForm, MessageForm,LoginForm,RegisterForm 
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
    
    form = RoomForm()
    context = {'form': form}


    if request.method =='POST':
        form = RoomForm(request.POST)
        # print(request.POST)
         
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            form.save()
            messages.success(request, "Room created sucessfullyy")
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, "Could not create room \n Try again!")
            return redirect('home')

    else:
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




def logoutUser(request):
    try: 
        logout(request)
        messages.success(request, "Logged out sucessfully")

    except:
        messages.error(request, "Error Fatal \n Error logging out!!")


    return redirect('home')


def registerPage(request):
    form = RegisterForm()

    context = {'form': form}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        #print(f'LOG: POST data recieved!!: {request.POST}')
        if form.is_valid():

            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save() 
            login(request, user)

            return redirect('home')

        else:
            print(form.errors)
            messages.error(request, 'An error occurred during registration! \n Please try again')


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


def loginView(request):
    page = 'login'
    form = LoginForm()
    context = {'form': form, 'page' : page}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username').lower()
            password = request.POST.get('password')

            try:
                user = User.objects.get(username=username)

            except:
                messages.error(request, "User does not exist")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Log in sucessfull")
                return redirect('home')
            else:
                messages.error(request, 'The username and password combination is incorrect')
        else:
            messages.error(request, 'Invalid Form')
            print(form.errors)
    return render(request, 'base/login_register.html', context)
