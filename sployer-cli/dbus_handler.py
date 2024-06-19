import dbus
import sys


class DBusHandler:
    def __init__(self) -> None:
        self._get_dbus_interface()

    def _get_dbus_interface(self) -> None:
        """
        Returns the dbus interface for spotify if it is running, otherwise exits
        """
        self.session_bus = dbus.SessionBus()

        try:
            interface = dbus.Interface(
                self.session_bus.get_object(
                    "org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2"
                ),
                "org.mpris.MediaPlayer2.Player",
            )
        except dbus.exceptions.DBusException:
            # If we catch this exception, Spotify is not running.
            sys.exit(
                "\nSome errors occured. Try restart or start Spotify. Pytify is just a cli application which controls Spotify. So you can't use Pytify without Spotify.\n"
            )
        self.interface = interface

    def _get_metadata(self):
        """
        Update the `self.metadate` variable
        """
        self.metadata = self.interface.Get("org.mpris.MediaPlayer2.Player", "Metadata")

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
