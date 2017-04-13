#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Cory Locklear
# Copyright (c) 2017 Cory Locklear
#
# License: MIT
#

"""This module exports the Staticcheck plugin class."""

from SublimeLinter.lint import Linter, util


class Staticcheck(Linter):
    """Provides an interface to staticcheck."""

    syntax = ('go', 'gosublime-go')
    cmd = 'staticcheck'
    regex = r'^.+:(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'
    tempfile_suffix = 'staticcheck'
    error_stream = util.STREAM_STDOUT
