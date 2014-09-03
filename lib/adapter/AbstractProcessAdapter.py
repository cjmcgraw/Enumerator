"""Describes the AbstractProcessAdapter
interface
"""
from abc import ABCMeta, abstractmethod


class AbstractProcessAdapter(object):
    """AbstractProcessAdapter defines
    the required functionality for an
    object to be a useable ProcessAdapter
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self, command, *args, **flags):
        """Executes the given string
        command, with the given flags

        @param command: str representing
        the command to be executed

        @param args: arg represent arguments
        that are to be passed to the command
        in the given order

        @keyword flags: keyword catchall that
        represents the flags. Each flag is given
        as a key value pair, representing the
        flag and the associated value respectively.
        All flags will be parsed into their respective
        prefix and should be without them when passed
        to this method. If you wish a simple flag to
        be called without any value simply give it a
        True value, which will be interpreted as the
        flag standing alone. False however will call
        the flag with the False value

        @return bool: representing if the call was
        successfully made or not
        """
        pass
