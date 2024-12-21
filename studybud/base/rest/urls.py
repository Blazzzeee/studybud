from django.urls import path
from . import views

urlpatterns = [
    path('', views.routes),
    path('rooms/', views.apiRooms ),
    path('rooms/<str:id>', views.apiRoom ),


]
