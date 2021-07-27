#!/usr/bin/env python3

"""
Application - The way to make things right.
Usage:
  application.py arg1 [--arg2 <key>]
  application.py (-h | --help)
  application.py --version
Options:
  -h, --help    Show this screen.
  --version     Show version.
  --arg2 <key>  Another argument [default: 42].
"""

__author__ = 'Road Runner, Willy Coyote'
__copyright__ = 'Copyright 2014, Acme Inc.'
__credits__ = ['Road Runner', 'Road Runners best friend Harrold']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Road Runners other friend Herb'
__email__ = 'appteam@acme.com'
__status__ = 'Development'

import os
import sys
import getpass

import docopt

#import myotherclass


class MainClass:
    """
    Main class which holds this and that and does this and that.
    """
    def __init__(self):
        """
        Initialize main class with this and that.
        """
        self._location = os.path.abspath('.')
        self._username = getpass.getuser()

    def whereami(self):
        """
        Display our current path.
        """
        print(self._location)

    def whoami(self):
        """
        Display the user who executes this program.
        """
        print self._username


if __name__ == '__main__':
    ARGS = docopt.docopt(__doc__, version='Application %s' % __version__)
    APP = MainClass()
    sys.exit(APP.whoami())
