from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
#from rest_framework_simplejwt import api_settings
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer, TokenSerializer

#jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Create your views here.

class MusicLibraryView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PlaylistsView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DetailSongView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    # This permission class will overide the global permission
    # class setting
    #permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()
    serializer_class = TokenSerializer
    permission_classes = (permissions.AllowAny,)
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                #"token": jwt_encode_handler(
                 #   jwt_payload_handler(user)
                #)
                })
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

