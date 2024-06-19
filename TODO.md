# Documentation
https://specifications.freedesktop.org/mpris-spec/latest/Player_Interface.html

1. Be able to change the volume. Proof:
>>> dbus_handler.properties.Set("org.mpris.MediaPlayer2.Player", "Volume", dbus.Double(0.5))