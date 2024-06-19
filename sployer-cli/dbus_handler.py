import dbus
import sys


class DBusHandler:
    def __init__(self) -> None:
        # Get the dbus proxy

        self.session_bus = dbus.SessionBus()

        self.interface = self.get_interface("org.mpris.MediaPlayer2.Player")
        self.properties = self.get_interface("org.freedesktop.DBus.Properties")

    def get_interface(self, interface):
        try:
            interface = dbus.Interface(
                self.session_bus.get_object(
                    "org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2"
                ),
                interface,
            )
        except dbus.exceptions.DBusException:
            # If we catch this exception, Spotify is not running.
            sys.exit(
                "\nSpotify was not found. Try restarting/opening it. This program requires Spotify APPLICATION open.\n"
            )

        return interface

    def _get_metadata(self):
        """
        Update the `self.metadate` variable
        """
        self.metadata = self.properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

    def get_current_playing(self):
        """
        Returns the current playing song from the dbus
        """
        self._get_metadata()  # TODO: double check that this has to be run every time
        playing = {}

        for key, value in self.metadata.items():
            if key == "xesam:album":
                playing["album"] = value

            elif key == "xesam:title":
                playing["title"] = value

            elif key == "xesam:artist":
                playing["artist"] = value[0]

        return "%s - %s [%s]" % (playing["artist"], playing["title"], playing["album"])
