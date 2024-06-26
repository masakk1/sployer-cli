# Spotzero
spotzero is a command line interface as well as a package to control Spotify on *linux*

# Installing
spotzero uses `dbus-python`, and this package requires a some packages.
I can't be bothered to find every package for every distribution, so just try to 
`pip install dbus-python` as see what package says its missing.

## From pipy
> [!warn] 
> This isn't done yet
```bash
pip install spotzero
```

## From source
If you want to install from source you'll need some packages beacuse `dbus-python` requires it.
There are 2 methods from source:
1. Using the `--editable` flatg
2. Building it with `python -m build` and then installing it `pip install dist/spotzero-<latest_version>-py3-none-any.whl`

### 1. Installing dependencies for Distros
#### Every distro
For some reason meson sometimes installs a previous version.
```bash
pip install meson --upgrade
```

#### Ubuntu
```bash
apt install pip, git, meson, pkg-config, libdbus-1-dev, libglib2.0-dev
```
> add sudo as needed here.

### 2. Cloning the repo
```bash
git clone https://github.com/masakk1/spotzero.git
cd spotzero
```
### 3.A Installing for regular use (RECOMMENDED)
Install this way if you're only interested in using the program and not editing the source code.
```bash
pip install build # Make sure build is installed
python -m build . # Compile
pip install dist/spotzero-<LATEST_VERSION>-py3-none-any.whl
```

### 3.B Installing to edit the source code
Only do this if you want to contribute or edit the source code.
Once you move the foler, *spotzero* will not work anymore.
The reason why I use `--editable` is because in many distros `pip install .` doesn't work.
```bash
# You should probably make a venv first.
python -m venv . # or make a venv with your IDE of choice (RECOMMENDED).
                 # you might need to install python3.10-venv whatever your distro
                 # complains with
pip install --editable .
```

# Usage
## From the terminal - CLI
```bash
spotzero # This will show the possible commands

# Lets play a song
spotzero play_uri "spotify:track:6vWZUOcDySwffRBcxlIFNr"

# I'm tired of it, pause it
spotzero toggle-play
```
That's it. It will show all the possible commands

## As a pyton library
```python
import spotzero.cli as spotzero

spotzero.pause()
spotzero.play_uri("spotify:track:4iV5W9uYEdYUVa79Axb7Rh")
```
Or you could also import the spotzero.linux module - in case there happens to be a function not available in the CLI in the future.

# Contributing
If you want more of this, make sure to open a pull request with your changes! - *I did this project in 3 days so it's pretty easy*

## Want to add more functions?
This project relies on dbus-python, dbus_handler.py is the one in charge of interacting with the dbus shenanigans. If you want to use another method: check out https://specifications.freedesktop.org/mpris-spec/latest/Player_Interface.html - you can also change properties - dbus_handler is somewhat documented so check that too.

## Want to add another platform?
There is a linux.py module right now. You could try adding a windows.py module but I don't have a proper way to change it. Shouldn't be too hard, look at the original project I forked from.