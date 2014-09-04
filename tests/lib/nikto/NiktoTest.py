"""This package defines the NiktoTest
class that is used for unit testing
the Nikto class

@author: Carl McGraw
@contact: cjmcgraw(- at -)u.washington.edu
@version: 1.x
"""
import unittest

from lib.nikto.Nikto import Nikto, REQUIRED_NIKTO_VERSION

from tests.lib.adapter.OSPathAdapterMock import OSPathAdapterMock
from tests.lib.adapter.ProcessAdapterMock import ProcessAdapterMock
from tests.lib.adapter.PopenMock import PopenMock


class NiktoTest(unittest.TestCase):
    """Utilized for unit testing the
    Nikto class"""

    def setUp(self):
        self.process_adapter = ProcessAdapterMock()
        self.ospath_adapter = OSPathAdapterMock()

        self.process_result = PopenMock()
        self.process_adapter.return_data = self.process_result

        self.nikto = Nikto(process_adapter=self.process_adapter,
                           ospath_adapter=self.ospath_adapter)

    def tearDown(self):
        del self.nikto
        del self.process_adapter
        del self.ospath_adapter

    def test_nikto_verified_identical_nikto_version(self):
        # Arrange
        self._set_version_value(*REQUIRED_NIKTO_VERSION)

        # Apply + Assert
        Nikto(process_adapter=self.process_adapter)

    def test_nikto_verified_greater_nikto_version(self):
        # Arrange
        self._set_version_value(100, 1, 1)

        # Apply + Assert
        Nikto(process_adapter=self.process_adapter)

    def test_nikto_verified_lower_nikto_version_all_version_types(self):
        # Arrange
        self._set_version_value(1, 1, 1)

        # Apply + Assert
        self.assertRaises(OSError, Nikto, process_adapter=self.process_adapter)

    def test_nikto_verified_lower_only_main_is_lower(self):
        # Arrange
        self._set_version_value(REQUIRED_NIKTO_VERSION[0] - 1, 100, 100)

        # Apply + Assert
        self.assertRaises(OSError, Nikto, process_adapter=self.process_adapter)

    def test_nikto_verified_lower_only_major_is_lower(self):
        # Arrange
        self._set_version_value(REQUIRED_NIKTO_VERSION[0], REQUIRED_NIKTO_VERSION[1] - 1, 100)

        # Apply + Assert
        self.assertRaises(OSError, Nikto, process_adapter=self.process_adapter)

    def test_nikto_verified_lower_only_minor_is_lower(self):
        # Arrange
        self._set_version_value(REQUIRED_NIKTO_VERSION[0], REQUIRED_NIKTO_VERSION[1], REQUIRED_NIKTO_VERSION[2] - 1)

        # Apply + Assert
        self.assertRaises(OSError, Nikto, process_adapter=self.process_adapter)

    def _set_version_value(self, *args):
        # Arrange
        version = [""] * 5 + ["nikto main   {}.{}.{}".format(*args)]
        self.process_adapter.POPEN_VERSION.stdout = version

    def test_scan_command_is_correctly_passed_to_process_adapter__command_matches(self):
        # Apply
        self.nikto.scan("")

        # Assert
        self.assertEquals(Nikto.NIKTO_COMMAND, self.process_adapter.command)

    def test_scan_command_is_correctly_passed_to_process_adapter__host_flag_matches(self):
        # Arrange
        host = "123.456.789"

        # Apply
        self.nikto.scan(host)

        # Assert
        self.assertEquals({"host": host}, self.process_adapter.flags)

    def test_scan_command_is_correctly_passed_to_process_adapter__output_flag_matches(self):
        # Arrange
        host = "scooby doo"
        output_file = "some output file"

        # Apply
        self.nikto.set_output(output_file)
        self.nikto.scan(host)

        # Assert
        self.assertEquals({"host": host, "output": output_file}, self.process_adapter.flags)

    def test_scan_command_is_correctly_passed_to_process_adapter__all_areas_match(self):
        # Arrange
        host = "scooby doo"
        output = "some output"

        # Apply
        self.nikto.set_output(output)
        self.nikto.scan(host)

        # Assert
        self.assertEquals(Nikto.NIKTO_COMMAND, self.process_adapter.command)
        self.assertEquals(tuple(), self.process_adapter.args)
        self.assertEquals({"host": host, "output": output}, self.process_adapter.flags)

    def test_scan_popen_object_is_returned(self):
        # Arrange
        popen = PopenMock()
        self.process_adapter.return_data = popen

        # Apply
        process = self.nikto.scan("some host")

        # Assert
        self.assertEquals(hash(popen), hash(process))

    def test_set_output_valid_output(self):
        # Apply
        self.nikto.set_output("some output file")

        # Assert
        self.assertEquals("some output file", self.ospath_adapter.dir_data)

    def test_set_output_invalid_output(self):
        # Arrange
        self.ospath_adapter.dir_response = False

        # Apply + Assert
        self.assertRaises(IOError, self.nikto.set_output, "some output file")


if __name__ == "__main__":
    unittest.main()