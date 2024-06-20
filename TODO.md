# Documentation
https://specifications.freedesktop.org/mpris-spec/latest/Player_Interface.html

1. Figure out how to publish as a pipy package
2. Add a README.md
   1. Add a small tutorial on how to install
   2. another on how to use as a cli
   3. lastly, how to use as a package
3. Write tests (how?)
4. Fix pip install . not working without --editable tag
5. Fix prev_song() on cli calling skip_song() on lib
6. Add requirements package for Ubuntu: 
   1. APT: pip, git, meson, python3.10-venv, pkg-config, libdbus-1-dev, libglib2.0-dev
   2. FOR SOME REASON MESON INSTALLS A PREVIOUS VERSION. pip install meson --upgrade
