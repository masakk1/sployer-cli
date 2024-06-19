from __future__ import absolute_import, unicode_literals
import db
import sys

import dbus.interface


class Interface():
    def factory(type):
        session_bus = pythondbus.

        try:
            interface = dbus.interface(
                dbus.SessionBus().get_object(
                    'org.mpris.MediaPlayer2.spotify',
                    '/org/mpris/MediaPlayer2'
                ),
                type
            )
        except dbus.exceptions.DBusException:
            """
                If we catch this exception, Spotify is not running.
                Let the user know.
            """
            sys.exit(
                "\nSome errors occured. Try restart or start Spotify. Pytify is just a cli application which controls Spotify. So you can't use Pytify without Spotify.\n"
            )

        return interface
    factory = staticmethod(factory)
