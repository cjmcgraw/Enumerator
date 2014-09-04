"""This module defines the ProcessAdapter
class that is used to abstract the execution
of commands.

@author: Carl McGraw
@contact: cjmcgraw(- at -)u.washington.edu
@version: 1.0
"""
from subprocess import check_call
from .AbstractProcessAdapter import AbstractProcessAdapter


class ProcessAdapter(AbstractProcessAdapter):
    """Allows for users to str commands with
    flags and args without having to invoke
    the subprocess module
    """
    SIMPLE_FLAG_PREFIX = "-"
    COMPLEX_FLAG_PREFIX = "--"

    def execute(self, command, *args, **flags):
        """Executes the given command, with the
        given args and flags.

        @param command: str representing the
        command to be executed

        @param args: catchall for all str args
        to be passed to the command, not as flags.
        The arguments will only be called in the
        exact order they are given

        @keyword flags: catchall for all str
        keywords to be passed. If setting a
        value to just a  single flag, give
        the result as True and it will be
        invoked only as the flag. All flags
        are called via a dictionary and thus
        ordering is approximately random.
        Furthermore please don't include dashes
        before flag arguments ("-", "--") as
        the system will include them automatically

        @return bool: representing if the call was
        successful or not.
        """
        cmnds = (command,) + args + self._parse_flags(**flags)
        return_code = self._execute(cmnds)
        return bool(return_code)

    def _execute(self, cmds):
        """Executes the command

        @param cmds: list of str
        representing the commands
        to be executed

        @return: int representing
         the return code of the call
        """
        return check_call(cmds)

    def _parse_flags(self, **flags):
        """Parses the flag arguments into
        a list of strs that are of the format
        "-f data" or "--flag data" respectively.

        @keyword flags: catchal for all str keywords.
        Values will be casted to Str type via the str
        command

        @return list: list of str representing each
        flag value pair
        """
        result = []

        for flag, value in flags.items():
            prefix = self.COMPLEX_FLAG_PREFIX if (len(flag) > 1) else self.SIMPLE_FLAG_PREFIX
            result.append(prefix + flag)

            if value is not True:
                result.append(str(value))

        return tuple(result)
