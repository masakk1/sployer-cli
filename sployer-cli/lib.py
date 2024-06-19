import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dbus_handler import DBusHandler

dbus_handler = DBusHandler()


scope = "playlist-modify-private playlist-modify-public playlist-read-private playlist-read-collaborative playlist-read-private playlist-read-collaborative user-library-modify user-library-read"
sp_api: spotipy.Spotify = None


def connect_to_spotify():
    global sp_api
    sp_api = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    print("Connected to Spotify")


def get_song_uri_at_index(self, index):
    return str(self._songs[index]["href"])


def get_song_name_at_index(self, index):
    return str("%s - %s" % (self._songs[index]["artist"], self._songs[index]["song"]))


def play_uri(uri: str):
    dbus_handler.interface.OpenUri(uri)


def skip_song():
    dbus_handler.interface.Next()


def prev_song():
    dbus_handler.interface.Previous()


def toggle_play():
    dbus_handler.interface.PlayPause()


def resume():
    dbus_handler.interface.Play()


def pause():
    dbus_handler.interface.Stop()
