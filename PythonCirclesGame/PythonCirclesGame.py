# PythonCirclesGame.py - Entry point to application.
# Created by Josh Kennedy on 17 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import GameInit

import platform
import sys

__version__ = "0.1.5"


# We want to check that we're running CPython 3.4.4 and not anything older or not CPython.
def python_version_check():
    # Grab the Python version.
    first = int(platform.python_version_tuple()[0])
    second = int(platform.python_version_tuple()[1])
    third = int(platform.python_version_tuple()[2])

    # Ensure that they're using the CPython implementation
    if platform.python_implementation() is not "CPython":
        print("You must use the CPython implementation of Python!\n\n")
        sys.exit(1)

    # Detect Python version, so we can alert the user if they're using an older version.
    if first < 3 or second < 5:
        print("You need Python 3.5 to play this game!\n\n")
        sys.exit(2)

    # We need to warn the user if they're using an older version of Python 3.5 to ensure the best experience.
    if first is 3 and second is 5 and third < 2:
        print("It is EXTREMELY recommended that you use the latest version of Python 3 "
              "(which is 3.5.2) to run this game!\n\n")

    # We also need to warn the user if they're using a newer version, because we can't guarantee it will work.
    if first > 3 or second > 5:
        print("It is recommended that you use Python 3.5 to play this game.\n"
              "We can't guarantee the stability and performance in newer versions of Python.\n\n")


# Our main function.
def main():
    python_version_check()

    print("Pop a Dots Version %s\nCopyright (C) 2014-2016 Sirkles LLC\n" % __version__)

    GameInit.initialize()
    GameInit.start()

# Our actual entry point.
if __name__ == "__main__":
    main()
