"""Describes the AbstractProcessAdapter
interface
"""
from abc import ABCMeta, abstractmethod

class AbstractProcessAdapter(Object):
    """AbstractProcessAdapter defines
    the required functionality for an
    object to be a useable ProcessAdapter
    """

    @abstractmethod
    def execute(command, **subcommands, **flags):
        """Executes the given string
        command, with the given flags.

        @param command: str representing
        the command to be executed

        @param subcommands: arg catchall
        these are subcommands that should
        be called as part of the main command.
        Each sub command will be called in the
        respective order given

        @keyword flags: keyword catchall
        that will catch all the flags to
        be called on this command. Flags
        are called in a randomly decided order
        and each flag is called with a '-'leading
        its name
        """
        pass
