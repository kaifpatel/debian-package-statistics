import unittest
import logging
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch
from package_statistics import count_files_per_package, display_top_packages, parse_arguments

class TestPackageStatistics(unittest.TestCase):
    
    def setUp(self):
        # Printing a horizontal line before each test for readability
        print("\n" + "-" * 50)
        
        # Capturing logs for each test for consistency with main script logging
        self.log_output = StringIO()
        logging.basicConfig(stream=self.log_output, level=logging.INFO)


    def test_count_files_per_package(self):
        # Mocking input data, simulating lines from a Contents file
        lines = [
            "/path/to/file1 package1",
            "/path/to/file2 package1",
            "/path/to/file3 package2",
            "/path/to/file4 package2",
            "/path/to/file5 package2",
        ]
        
        expected_counts = {
            "package1": 2,
            "package2": 3,
        }
        
        # Calling the function and comparing the result
        result = count_files_per_package(lines)
        self.assertEqual(result, expected_counts)


    def test_count_files_empty_input(self):
        # Testing with empty input
        lines = []
        expected_counts = {}
        result = count_files_per_package(lines)
        self.assertEqual(result, expected_counts)


    def test_count_files_single_line_multiple_packages(self):
        # Testing with a single line containing multiple packages
        lines = ["/path/to/file1 package1 package2 package3"]
        expected_counts = {
            "package1": 1,
            "package2": 1,
            "package3": 1,
        }
        result = count_files_per_package(lines)
        self.assertEqual(result, expected_counts)


    def test_display_top_packages(self):
        # Mocking input data
        package_counts = {
            "package1": 5,
            "package2": 3,
        }

        # Capturing the actual output of the display_top_packages function
        with StringIO() as buf, redirect_stdout(buf):
            display_top_packages(package_counts, top_n=2)
            output = buf.getvalue()

        # Mocking output format
        expected_output = (
            "\nTop 10 Packages by Number of Files:\n"
            "package1      5\n"
            "package2      3\n"
            "\n"
        )

        # Asserting the output matches the expected format
        self.assertEqual(output, expected_output)


    def test_parse_arguments_valid_architecture(self):
        # Simulating valid command-line arguments with 'amd64' as input
        with patch("sys.argv", ["package_statistics.py", "amd64"]):
            args = parse_arguments()
            self.assertEqual(args.architecture, "amd64")


    def test_parse_arguments_invalid_architecture(self):
        # Simulating an invalid architecture argument and check if SystemExit is raised
        with patch("sys.argv", ["package_statistics.py", "example_invalid_arch"]):
            with self.assertRaises(SystemExit) as cm:
                parse_arguments()

    def tearDown(self):
        # Outputting log content if needed for additional test insights
        log_content = self.log_output.getvalue()
        if log_content.strip():
            print("Log output:\n", log_content)
        else:
            print("Log output: No additional log messages. Test ran successfully.")

        # Adding a new line after "ok" for readability
        print("\n")

if __name__ == "__main__":
    unittest.main()
