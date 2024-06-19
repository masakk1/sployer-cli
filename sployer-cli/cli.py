import click
from dbus_handler import DBusHandler

dbus_handler = DBusHandler()


def get_song_uri_at_index(self, index):
    return str(self._songs[index]["href"])


def get_song_name_at_index(self, index):
    return str("%s - %s" % (self._songs[index]["artist"], self._songs[index]["song"]))


@click.group()
def cli():
    pass


@cli.command()
@click.argument("index", type=click.INT, required=True)
def play_song(index):
    dbus_handler.interface.OpenUri(get_song_uri_at_index(index))


@cli.command()
def skip_song():
    dbus_handler.interface.Next()


@cli.command()
def prev_song():
    dbus_handler.interface.Previous()


@cli.command()
def toggle_play():
    dbus_handler.interface.PlayPause()


@cli.command()
def pause():
    dbus_handler.interface.Stop()


if __name__ == "__main__":
    cli = click.CommandCollection(click.Group("cli"), [cli])
    cli()
