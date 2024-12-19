from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Room
from .serializers import RoomSerializer



@api_view(['GET', ])
def routes(request):
    routes = [
        'GET api/',
        'GET api/rooms',
        'GET api/rooms/:id'

    ]

    return Response(routes)

@api_view(['GET', ])
def apiRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def apiRoom(request, id):
    room = Room.objects.get(pk=id)
    serializer = RoomSerializer(room, many=False)

    return Response(serializer.data)
