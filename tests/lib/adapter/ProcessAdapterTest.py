"""This module provides the testing class for
ProcessAdapterTest

@author: Carl McGraw
@contact: cjmcgraw(- at -)u.washington.edu
@version: 1.0
"""
from unittest import TestCase, main

from lib.adapter.ProcessAdapter import ProcessAdapter


class ProcessAdapterTest(TestCase, ProcessAdapter):
    """This class provides the testing case for
    the ProcessAdapter class. Since the ProcessAdapter
    is a lower level operation that calls a python
    library it was necessary to subclass the class
    to test it so that the calls to the _execute
    method could be overridden and intercepted to
    check what commands are passed to the python
    library.
    """
    ARGS = tuple(["arg" + str(x) for x in range(10)])

    def setUp(self):
        self._executions = []

    def test_execute_single_command(self):
        # Set up
        expected = ("someCommand",)

        # Test
        self.__test_execute(expected, "someCommand")

    def test_execute_with_single_argument(self):
        # Set up
        expected = ("commandWithOneArg", self.ARGS[0])

        # Test
        self.__test_execute(expected, *expected)

    def test_execute_with_two_arguments(self):
        # Set up
        expected = ("commandWithTwoArgs",) + self.ARGS[:2]

        # Test
        self.__test_execute(expected, *expected)

    def test_execute_with_three_arguments(self):
        # Set up
        expected = ("commandWithThreeArgs",) + self.ARGS[:3]

        # Test
        self.__test_execute(expected, *expected)

    def test_execute_with_one_flag(self):
        # Set up
        cmd = "commandWithSingleFlag"
        expected = (cmd, "-x")

        # Test
        self.__test_execute(expected, cmd, x=True)

    def test_execute_with_two_flag(self):
        # Set up
        cmd = "commandWithTwoFlags"
        expected = (cmd, "-x", "-y")

        # Test
        self.__test_execute(expected, cmd, x=True, y=True)

    def test_execute_with_three_flags(self):
        # Set up
        cmd = "commandWithThreeFlags"
        expected = (cmd, "-x", "-y", "-z")

        # Test
        self.__test_execute(expected, cmd, x=True, y=True, z=True)

    def test_execute_with_one_flag_and_value(self):
        # Set up
        cmd = "commandWithOneFlagAndValue"
        expected = (cmd, "-f", "1")

        # Test
        self.__test_execute(expected, cmd, f=1)

    def test_execute_with_two_flags_and_values(self):
        # Set up
        cmd = "commandWithTwoFlagsAndValues"
        expected = (cmd, "-f", "1", "-g", "2")

        #Test
        self.__test_execute(expected, cmd, f=1, g=2)

    def test_execute_with_three_flags_and_values(self):
        # Set up
        cmd = "commandWithThreeFlagsAndValues"
        expected = (cmd, "-f", "1", "-g", "2", "-h", "3")

        # Test
        self.__test_execute(expected, cmd, f=1, g=2, h=3)

    def test_execute_with_one_arg_one_flag(self):
        # Set up
        cmd = "commandWithArgAndFlag"
        expected = (cmd, self.ARGS[0], "-f")

        # Test
        self.__test_execute(expected, cmd, self.ARGS[0], f=True)

    def test_execute_with_two_args_two_flags(self):
        # Set up
        cmd = "commandWithTwoArgsAndTwoFlags"
        expected = (cmd,) + self.ARGS[:2] + ("-f", "-g")

        # Test
        self.__test_execute(expected, cmd, *self.ARGS[:2], f=True, g=True)

    def test_execute_with_three_args_three_flags(self):
        # Set up
        cmd = "commandWithThreeArgsAndThreeFlags"
        expected = (cmd,) + self.ARGS[:3] + ("-f", "-g", "-h")

        # Test
        self.__test_execute(expected, cmd, *self.ARGS[:3], f=True, g=True, h=True)

    def test_execute_with_one_arg_and_one_flag_with_value(self):
        # Set up
        cmd = "commandWithOneARgAndOneFlagWithValue"
        expected = (cmd,) + (self.ARGS[0],) + ("-f", "1")

        # Test
        self.__test_execute(expected, cmd, self.ARGS[0], f=1)

    def test_execute_with_two_args_and_two_flags_with_values(self):
        # Set up
        cmd = "commandWithTwoArgsAndTwoFlagsWithValues"
        expected = (cmd,) + self.ARGS[:2] + ("-f", "1", "-g", "2")

        # Test
        self.__test_execute(expected, cmd, *self.ARGS[:2], f=1, g=2)

    def test_execute_with_three_args_and_three_flags_with_values(self):
        # Set up
        cmd = "commandWithThreeArgsAndThreeFlagsWithValues"
        expected = (cmd,) + self.ARGS[:3] + ("-f", "1", "-g", "2", "-h", "3")

        # Test
        self.__test_execute(expected, cmd, *self.ARGS[:3], f=1, g=2, h=3)

    def test_execute_with_flags_with_complex_values(self):
        # Set up
        cmd = "commandWithMultipleComplexArgs"
        expected = (cmd,) + ("-f", "False", "-g", "3.0", "-h", "some word")

        # Test
        self.__test_execute(expected, cmd, f=False, g=3.0, h="some word")

    def test_execute_with_one_keyword(self):
        # Set up
        cmd = "commandWithOneKeyword"
        expected = (cmd,) + ("--keyword0",)

        # Test
        self.__test_execute(expected, cmd, keyword0=True)

    def test_execute_with_two_keywords(self):
        # Set up
        cmd = "commandWithTwoKeyword"
        expected = (cmd,) + ("--keyword0", "--keyword1")

        # Test
        self.__test_execute(expected, cmd, keyword0=True, keyword1=True)

    def test_execute_with_three_keywords(self):
        # Set up
        cmd = "commandWithThreeKeyword"
        expected = (cmd,) + ("--keyword0", "--keyword1", "--keyword2")

        # Test
        self.__test_execute(expected, cmd, keyword0=True, keyword1=True, keyword2=True)

    def test_execute_with_one_arg_and_one_keyword(self):
        # Set up
        cmd = "commandWithOneArgAndOneKeyword"
        expected = (cmd, self.ARGS[0]) + ("--keyword0",)

        # Test
        self.__test_execute(expected, cmd, self.ARGS[0], keyword0=True)

    def test_execute_with_two_args_and_two_keywords(self):
        # Set up
        cmd = "commandWithTwoArgsAndTwoKeyword"
        expected = (cmd,) + self.ARGS[:2] + ("--keyword0", "--keyword1")

        # Test
        self.__test_execute(expected, cmd, *self.ARGS[:2], keyword0=True, keyword1=True)

    def test_execute_with_two_args_and_three_keywords(self):
        # Set up
        cmd = "commandWithThreeArgsAndThreeKeyword"
        expected = (cmd,) + self.ARGS[:3] + ("--keyword0", "--keyword1", "--keyword2")

        # Test
        self.__test_execute(expected, cmd, *self.ARGS[:3], keyword0=True, keyword1=True, keyword2=True)

    def test_execute_with_one_keyword_with_values(self):
        # Set up
        cmd = "commandWithOneKeywordWithValue"
        expected = (cmd,) + ("--keyword0", "1")

        # Test
        self.__test_execute(expected, cmd, keyword0=1)

    def test_execute_with_two_keywords_with_values(self):
        # Set up
        cmd = "commandWithTwoKeywordsWithValue"
        expected = (cmd,) + ("--keyword0", "1", "--keyword1", "2")

        # Test
        self.__test_execute(expected, cmd, keyword0=1, keyword1=2)

    def test_execute_with_three_keywords_with_values(self):
        # Set up
        cmd = "commandWithThreeKeywordsWithValues"
        expected = (cmd,) + ("--keyword0", "1", "--keyword1", "2", "--keyword2", "3")

        # Test
        self.__test_execute(expected, cmd, keyword0=1, keyword1=2, keyword2=3)

    def test_execute_with_one_arg_and_one_keyword_with_values(self):
        # Set up
        cmd = "commandWithOneArgAndOneKeywordWithValue"
        expected = (cmd, self.ARGS[0]) + ("--keyword0", "1")

        # Test
        self.__test_execute(expected, cmd, self.ARGS[0], keyword0=1)

    def test_execute_with_two_args_and_two_keywords_with_values(self):
        # Set up
        cmd = "commandWithTwoArgsAndTwoKeywordsWithValues"
        expected = (cmd,) + self.ARGS[:2] + ("--keyword0", "1", "--keyword1", "2")

        # Test
        self.__test_execute(expected, cmd, *self.ARGS[:2], keyword0=1, keyword1=2)

    def test_execute_with_three_args_and_three_keywords_with_values(self):
        # Set up
        cmd = "commandWithThreeArgsAndThreeKeywordsWithValues"
        expected = (cmd,) + self.ARGS[:3] + ("--keyword0", "1", "--keyword1", "2", "--keyword2", "3")

        # Test
        self.__test_execute(expected, cmd, *self.ARGS[:3], keyword0=1, keyword1=2, keyword2=3)

    def test_execute_with_keywords_with_complex_values(self):
        # Set up
        cmd = "commandWithMultiKeywordsAndComplexValues"
        expected = (cmd,) + ("--keyword0", "False", "--keyword1", "99.9", "--keyword2", "some words")

        # Test
        self.__test_execute(expected, cmd, keyword0=False, keyword1=99.9, keyword2="some words")

    def test_execute_with_one_arg_one_flag_one_keyword(self):
        # Set up
        cmd = "commandWithOneArgOneFlagOneKeyword"
        expected = (cmd, self.ARGS[0]) + ("-f", "--keyword0")

        # Test
        self.__test_execute(expected, cmd, self.ARGS[0], f=True, keyword0=True)

    def test_execute_with_two_ars_two_flags_two_keywords(self):
        # Set up
        cmd = "commandWithTwoArgsTwoFlagsTwoKeywords"
        expected = (cmd,) + self.ARGS[:2] + ("-f", "-g", "--keyword0", "--keyword1")

        # Test
        self.__test_execute(expected, cmd, *self.ARGS[:2], f=True, g=True, keyword0=True, keyword1=True)

    def test_execute_with_three_args_three_flags_three_keywords(self):
        # Set up
        cmd = "commandWithThreeArgsThreeFlagsThreeKeywords"
        expected = (cmd,) + self.ARGS[:3] + ("-f", "-g", "-h", "--keyword0", "--keyword1", "--keyword2")

        # Test
        self.__test_execute(expected, cmd, *self.ARGS[:3], f=True, g=True, h=True,
                            keyword0=True, keyword1=True, keyword2=True)

    def test_execute_with_one_arg_one_flag_one_keyword_with_values(self):

        # Set up
        cmd = "commandWithOneArgOneFlagOneKeywordWithValues"
        expected = (cmd, self.ARGS[0]) + ("-f", "some words", "--keyword0", "1")

        # Test
        self.__test_execute(expected, cmd, self.ARGS[0], f="some words", keyword0=1)

    def test_execute_with_two_ars_two_flags_two_keywords_with_values(self):
        # Set up
        cmd = "commandWithTwoArgsTwoFlagsTwoKeywordsWithValues"
        expected = (cmd,) + self.ARGS[:2] + ("-f", "1", "-g", "some words", "--keyword0", "2",
                                             "--keyword1", "some other words")

        # Test
        self.__test_execute(expected, cmd, *self.ARGS[:2], f=1, g="some words", keyword0=2, keyword1="some other words")

    def test_execute_with_three_args_three_flags_three_keywords_with_values(self):
        # Set up
        cmd = "commandWithThreeArgsThreeFlagsThreeKeywordsWithValues"
        expected = (cmd,) + self.ARGS[:3] + ("-f", "1", "-g", "False", "-h", "some words",
                                             "--keyword0", "2", "--keyword1", "False", "--keyword2", "some other words")

        # Test
        self.__test_execute(expected, cmd, *self.ARGS[:3], f=1, g=False, h="some words", keyword0=2, keyword1=False,
                            keyword2="some other words")

    def __test_execute(self, expected, cmd, *args, **kwargs):
        # Apply
        self.execute(cmd, *args, **kwargs)

        exp_cmd_str = expected[0]
        exp_args_str = expected[1:len(args) + 1]
        exp_flags_str = expected[len(args) + 1:]

        cmd_str = self._command_line_call[0]
        args_strs = self._command_line_call[1:len(args) + 1]
        flags_strs = self._command_line_call[len(args) + 1:]

        # Assert
        self.__test_cmd_matches(exp_cmd_str, cmd_str)
        self.__test_args_match(exp_args_str, args_strs)
        self.__test_flags_match(exp_flags_str, flags_strs)

    def __test_cmd_matches(self, expected, actual):
        self.assertEquals(expected, actual)

    def __test_args_match(self, expected, actual):
        self.assertEquals(expected, actual)

    def __test_flags_match(self, expected, actual):
        """This test has to be significantly more complex
        than the other tests. This is because flags are
        passed through a dictionary with key value pairs.

        These key value pairs of the dictionary are hashed
        and therefore the exact ordering of the flags cannot
        be determined.

        As such the values much be parsed and returned in
        a way such that they can be compared for equality.

        There is an important distinction here. If we simply
        utilized a set to compare the flags to each other it
        could be theoretically correct (all the flags exist)
        but the key value pairs would be off because of potential
        different orderings for each dict.

        Using the (k,v) pairs in a set resolves this problem
        """
        expected_set = self.__create_result_set(expected)
        actual_set = self.__create_result_set(actual)

        self.assertEquals(expected_set, actual_set)

    def __create_result_set(self, data):
        """This is the method that scans the
        given string and pulls all its flag
        value pairs as a tuple and places them
        in a set. That way only the relative
        location of flags can be tested and not
        their exact location
        """
        result = set()

        i = 0
        while i + 1 < len(data):
            key = data[i]
            value = data[i + 1]

            if not self.__check_if_key(value):
                entry = (key, value)
                i += 2
            else:
                entry = (key,)
                i += 1
            result.add(entry)

        if i < len(data):
            result.add((data[i],))

        return result

    def __check_if_key(self, data):
            return (data.startswith(ProcessAdapter.SIMPLE_FLAG_PREFIX) or
                    data.startswith(ProcessAdapter.COMPLEX_FLAG_PREFIX))

    def _execute(self, cmds):
        """Overrides the _execute private
        method of the superclass ProcessAdapter
        this allows for us to intercept calls to
        the command line calls and instead test
        them here

        @param cmds: str representing the
        commands to be passed to the command
        line
        """
        self._command_line_call = cmds

if __name__ == "__main__":
    main()