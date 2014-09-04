"""This module defines the Nikto class
that is used for scanning web servers

@author: Carl McGraw
@contact: cjmcgraw(- at -)u.washington.edu
@version: 1.0
"""
import re
import operator

from lib.adapter.ProcessAdapter import ProcessAdapter
from lib.adapter.OSPathAdapter import OSPathAdapter
from .AbstractNikto import AbstractNikto


NIKTO_VERSION_NAME = "nikto main"
REQUIRED_NIKTO_VERSION = (2, 1, 4)


class Nikto(AbstractNikto):
    """Nikto class is used for 
    web server scanning. This class
    has a hard requirement on the
    Nikto command for Linux
    """
    NIKTO_COMMAND = "nikto"
    VERSION_FLAG = "-Version"
    VERSION_SEPARATOR = "---"

    def __init__(self, process_adapter=None, ospath_adapter=None):
        """Initializes the Nikto object

        @keyword process_adapter: AbstractProcessAdapter
        subclass that is to be initialized as the process
        adapter for this Nikto

        @keyword ospath_adapter: OSPathAdapter class that
        is to be initialized as the path adapter.
        """
        self._output = None
        self._command_adapter = process_adapter if process_adapter else ProcessAdapter()
        self._os_path_adapter = ospath_adapter if ospath_adapter else OSPathAdapter()

        self._verify_nikto_present()

    def _verify_nikto_present(self):
        """Verifies that the nikto command
        is currently present
        """
        p = self._command_adapter.execute(self.NIKTO_COMMAND, self.VERSION_FLAG)
        version_data = self._parse_version_data(p)
        self._validate_current_nikto_version(version_data)

    def _parse_version_data(self, process):
        """Parses the current version data
        from the given process

        @param process: subprocess.Popen
        object that represents the process

        @return: dict of str to int tuple
        that represent package to version
        numbers
        """
        version_data = {}

        for line in self._parse_process_lines(process):
            name = line[0].lower()
            version = tuple(map(int, line[1].split(".")))
            version_data[name] = version

        return version_data

    def _parse_process_lines(self, process):
        """Parses the lines of the process to
        to retrieve the version data.

        @param process: subprocess.Popen
        object that represents the process

        @return: list of tuples representing
        the parsed lines from the process
        """
        return filter(lambda x: len(x) >= 2, [re.split("\s\s+", line.rstrip()) for line in process.stdout][5:])

    def _validate_current_nikto_version(self, version_data):
        """Validates the current version of nikto
        against the expected version.

        @raise OSError: if the found version of
        Nikto doesn't match the expected version

        @param version_data: dict of values
        representing the version data.
        """
        f = lambda x: sum(map(operator.mul, x, [10 ** 10, 10 * 10, 1]))

        actual = f(version_data[NIKTO_VERSION_NAME])
        expected = f(REQUIRED_NIKTO_VERSION)

        if actual < expected:
            msg = "invalid version of Nikto: need version greater than {}, found version {}!"
            found_version = "{}.{}.{}".format(*version_data[NIKTO_VERSION_NAME])
            exp_version = "{}.{}.{}".format(*REQUIRED_NIKTO_VERSION)
            raise OSError(msg.format(exp_version, found_version))

    def set_output(self, output_file):
        """Sets the output file to the
        given file.

        @raise IOError: if the given
        directory for the output file
        doesn't exist

        @param output_file: str representing
        the path to the output file
        """
        self._validate_output(output_file)
        self._output = output_file

    def _validate_output(self, output_file):
        """Validates the output file.

        @raise IOError: If the given output
        file directory doesn't exist

        @param output_file: str representing
        the output file
        """
        if not self._os_path_adapter.directory_exists(output_file):
            msg = "Output directory <{}> doesn't exist"
            raise IOError(msg.format(output_file))

    def scan(self, host):
        """Scans the given host
        and sends the output to the
        previously set output path.

        @param host: str representing
        the host to be scanned

        @return Popen: subprocess.Popen
        object that may be used to read
        the given data
        """
        kwargs = {"host": host}
        if self._output:
            kwargs["output"] = self._output
        return self._command_adapter.execute(self.NIKTO_COMMAND, **kwargs)