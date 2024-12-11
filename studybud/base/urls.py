from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('room/<str:id>', views.room, name='room'),
    path('create_room', views.create_room, name='create_room'),
    path('update_room/<str:id>', views.update_room, name='update_room'),
    path('delete_room/<str:id>', views.delete_room, name='delete_room'),
    path('login', views.loginView, name='login_register_form') 
    
]
