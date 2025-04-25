import unittest
import os
import sys
import re
import json
import tempfile
import datetime
import gzip
import urllib.request

from stdlib_demo import (
    get_current_directory,
    list_python_files,
    get_command_line_args,
    find_numbers,
    calculate_statistics,
    fetch_url_data,
    get_current_datetime,
    compress_data,
    measure_execution_time
)

class TestStdlibDemo(unittest.TestCase):

    def test_get_current_directory(self):
        cwd = get_current_directory()
        self.assertIsInstance(cwd, str)
        self.assertTrue(os.path.isdir(cwd))

    def test_list_python_files(self):
        # Create a temporary directory with some files.
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create some files.
            filenames = ["test1.py", "test2.txt", "script.py", "README.md"]
            for name in filenames:
                with open(os.path.join(temp_dir, name), "w") as f:
                    f.write("print('hello')")
            py_files = list_python_files(temp_dir)
            # Should only list the .py files.
            self.assertEqual(set(py_files), {"test1.py", "script.py"})

    def test_get_command_line_args(self):
        # Backup original sys.argv and modify temporarily.
        original_argv = sys.argv
        test_args = ["script.py", "arg1", "arg2"]
        sys.argv = test_args
        args = get_command_line_args()
        self.assertEqual(args, test_args)
        sys.argv = original_argv  # Restore original argv

    def test_find_numbers(self):
        text = "There are 15 cats, 7 dogs, and 42 birds."
        numbers = find_numbers(text)
        self.assertEqual(numbers, ["15", "7", "42"])

    def test_calculate_statistics(self):
        data = [10, 20, 30, 40, 50]
        stats = calculate_statistics(data)
        self.assertAlmostEqual(stats["mean"], 30)
        self.assertAlmostEqual(stats["median"], 30)
        self.assertAlmostEqual(stats["variance"], 250)

    def test_fetch_url_data(self):
        # Use a well-known URL; note that actual network calls might vary.
        url = "http://www.example.com"
        byte_count = 100
        data = fetch_url_data(url, byte_count)
        self.assertIsInstance(data, bytes)
        # The returned data might be less than byte_count if the resource is short.
        self.assertTrue(len(data) <= byte_count)

    def test_get_current_datetime(self):
        dt_str = get_current_datetime()
        # Check that the string matches the format YYYY-MM-DD HH:MM:SS.
        pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
        self.assertRegex(dt_str, pattern)

    def test_compress_data(self):
        original = b"This is some sample data to compress."
        compressed = compress_data(original)
        # Decompress and check equality.
        decompressed = gzip.decompress(compressed)
        self.assertEqual(decompressed, original)

    def test_measure_execution_time(self):
        # A simple code snippet to test.
        code = "x = 2 + 2"
        exec_time = measure_execution_time(code, 1000)
        self.assertIsInstance(exec_time, float)
        self.assertGreater(exec_time, 0)

if __name__ == "__main__":
    unittest.main()
