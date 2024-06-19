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
# TODO: Change this for my own help article
@click.help_option(
    "-h",
    "--help",
    help="https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids",
)
def play_uri(song_uri):
    lib.play_uri(song_uri)


@cli.command()
def skip_song():
    lib.skip_song()


@cli.command()
def prev_song():
    lib.skip_song()


@cli.command()
def toggle_play():
    lib.toggle_play()


@cli.command()
def resume():
    lib.resume()


@cli.command()
def pause():
    lib.pause()


if __name__ == "__main__":
    cli = click.CommandCollection(click.Group("cli"), [cli])
    cli()
