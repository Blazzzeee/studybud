from django.urls import path
from . import views

urlpatterns = [
    path('', views.routes, name='home'),
    path('rooms/', views.apiRooms, name='rooms'),
    path('rooms/<str:id>', views.apiRoom, name='room'),


]
