from django.urls import path
from .views import MusicLibraryView, PlaylistsView, DetailSongView, LoginView


urlpatterns = [
    path('library/', MusicLibraryView.as_view(), name="musiclibrary-songs"),
    path('songs/', PlaylistsView.as_view(), name="playlist-songs"),
    path('<int:pk>/', DetailSongView.as_view(), name="song-detail"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
]

