"""
    This py file allows to communicate with the backend
"""

import click
import lib


@click.group()
def cli():
    pass


@cli.command()
@click.argument("song_uri", type=click.STRING)
def play_uri(song_uri):
    """Plays spotify URIs - https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids"""
    lib.play_uri(song_uri)


@cli.command()
def skip_song():
    lib.skip_song()


@cli.command()
def prev_song():
    """Goes back to time 0 or previous song. Blame spotify not me"""
    lib.skip_song()


@cli.command()
def toggle_play():
    """Toggles between playing and paused."""
    lib.toggle_play()


@cli.command()
def resume():
    lib.resume()


@cli.command()
def pause():
    lib.pause()


@cli.command()
@click.argument("amount", type=float)
def change_volume(amount: float):
    """Adds (-- 0.5), or substracts (-- -0.7) volume"""
    lib.change_volume(amount)


@cli.command()
@click.argument("value", type=float)
def set_volume(value: float):
    """Sets volume between 0 and 1"""
    lib.set_volume(value)


if __name__ == "__main__":
    cli = click.CommandCollection(click.Group("cli"), [cli])
    cli()
