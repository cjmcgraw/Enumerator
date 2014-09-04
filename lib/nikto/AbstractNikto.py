"""This module defines the 
abstract interface AbstractNikto

@author: Carl McGraw
@contact: cjmcgraw(- at -)u.washington.edu
@version: 1.0
"""

from abc import ABCMeta, abstractmethod


class AbstractNikto(object):
    """This class defines the required
    functionality for an object to be
    a useable Nikto
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def set_output(self, output_file):
        """Sets the output for
        the commands utilized
        
        @param output_file: str
        representing the output
        file to be written to.
        """
        pass

    @abstractmethod
    def scan(self, host):
        """Scans the given host.
        
        @param host: str representing
        the IP address of the host to
        be scanned.

        @return bool: representing if
        the test successful printed
        to the output.
        """
        pass
