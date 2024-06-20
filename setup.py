from setuptools import setup

setup(
    name="spotzero",
    version="0.1.0",
    py_modules=["spotzero"],
    install_requires=["dbus-python==1.3.2", "click>=8.1"],
    entry_points={
        "console_scripts": [
            "spotzero = spotzero.cli:cli",
        ],
    },
)
