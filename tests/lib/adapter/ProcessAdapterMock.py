"""This package describes the
ProcessAdapterMock class used
for testing

@author: Carl McGraw
@contact: cjmcgraw(- at -)u.washington.edu
@version: 1.x
"""
from lib.adapter.AbstractProcessAdapter import AbstractProcessAdapter
from .PopenMock import PopenMock

from lib.nikto.Nikto import Nikto, NIKTO_VERSION_NAME


class ProcessAdapterMock(AbstractProcessAdapter):
    """ProcessAdapterMock is used to mocking
    out the normal ProcessAdapter and feeding
    pre-set responses and recording input
    """
    VERSION_DATA = [""] * 5 + [NIKTO_VERSION_NAME + "    99.99.99"]
    POPEN_VERSION = PopenMock()

    def __init__(self):
        """Initializes the mock object"""
        self.POPEN_VERSION.stdout = self.VERSION_DATA
        self.command = None
        self.args = None
        self.flags = None

        self.return_data = None

    def execute(self, command, *args, **flags):
        """Records the given parameters and
        emits the pre set data

        @param command: str representing the
        command

        @param args: catchall for each str
        argument to be passed to the command

        @param flags: catchall for each flag
        argument to be passed to the command

        @return: subprocess.Popen
        """
        if Nikto.VERSION_FLAG in args:
            return self.POPEN_VERSION
        else:
            self.command = command
            self.args = args
            self.flags = flags
            return self.return_data