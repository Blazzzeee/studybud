from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings 

urlpatterns = [
    path('', views.home , name='home'),
    path('room/<str:id>', views.room, name='room'),
    path('create_room', views.create_room, name='create_room'),
    path('update_room/<str:id>', views.update_room, name='update_room'),
    path('delete_room/<str:id>', views.delete_room, name='delete_room'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerPage, name='register'),
    path('recent', views.recent_page, name='recent'),
    path('test', views.testView, name='test')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
