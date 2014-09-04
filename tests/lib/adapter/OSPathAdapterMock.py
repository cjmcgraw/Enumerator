"""OSPathAdapter mock that is used to
pass mock data to a file regarding
the OSPath

@author: Carl McGraw
@contact: cjmcgraw(- at -)u.washington.edu
@version: 1.x
"""


class OSPathAdapterMock(object):
    """Mock object is utilized in testing
    to control the input and output
    """

    def __init__(self):
        """Initializes the adapter"""
        self.dir_data = None
        self.dir_response = True
        self.path_data = None
        self.path_response = True

    def directory_exists(self, path):
        """Records directory path given
        and emits the set response

        @param path: str representing
        the path.

        @return: bool
        """
        self.dir_data = path
        return self.dir_response

    def path_exists(self, path):
        """Records the path given
        and emits the set response

        @param path: str representing
        the path

        @return: bool
        """
        self.path_data = path
        return self.path_response
