"""This package provides the OSAdapter class
that is used to wrap the OS.path calls under
a layer of abstraction

@author: Carl McGraw
@contact: cjmcgraw(- at -)u.washington.edu
@version: 1.x
"""
from os.path import exists, dirname, isdir


class OSPathAdapter(object):
    """OSPathAdapter class wraps
    the calls to the os.path library
    under a layer of abstraction to
    allow for better unit testing
    """

    def directory_exists(self, path):
        """Checks if the given directory
        contained in the path exists.

        @param path: str representing the
        path whose directories are to be
        checked if they exist. This can either
        be the path directly to the directory,
        or the path to the file which may not
        yet exist.

        @return: bool representing if the
        specified directories in the given
        path exist.
        """
        if isdir(path):
            self.path_exists(path)
        else:
            self.path_exists(dirname(path))

    def path_exists(self, path):
        """Checks if the given path exists

        @param path: str representing the
        path to check

        @return: bool representing if the
        given path exists
        """
        return exists(path)