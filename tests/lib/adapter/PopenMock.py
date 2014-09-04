"""This package provides the
PopenMock class used for passing
data for testing

@author: Carl McGraw
@contact: cjmcgraw(- at -)u.washington.edu
@version: 1.x
"""


class PopenMock(object):
    """PopenMock class is to be
    used when testing classes that
    utilize Popen
    """

    def __init__(self):
        """Initializes the PopenMock"""
        self.stdout = []
        self.stderr = []
        self.stdin = []
