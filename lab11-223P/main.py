import stdlib_demo
import unittest


def demonstrate_functions():
    """Demonstrate all functions from the stdlib_demo module."""
    print("\n===== STDLIB DEMO FUNCTIONS =====\n")
    
    # 1. Testing get_current_directory
    print("1. Current Directory:")
    current_dir = stdlib_demo.get_current_directory()
    print(f"   {current_dir}\n")
    
    # 2. Testing list_python_files
    print("2. Python Files in Current Directory:")
    python_files = stdlib_demo.list_python_files(current_dir)
    for file in python_files:
        print(f"   - {file}")
    print()
    
    # 3. Testing get_command_line_args
    print("3. Command Line Arguments:")
    args = stdlib_demo.get_command_line_args()
    for i, arg in enumerate(args):
        print(f"   Arg {i}: {arg}")
    print()
    
    # 4. Testing find_numbers
    print("4. Finding Numbers in Text:")
    sample_text = "The price is $42.99 and the quantity is 5, so the total is $214.95."
    numbers = stdlib_demo.find_numbers(sample_text)
    print(f"   Text: '{sample_text}'")
    print(f"   Numbers found: {numbers}\n")
    
    # 5. Testing calculate_statistics
    print("5. Calculating Statistics:")
    data = [12, 15, 18, 22, 25, 28, 30]
    stats = stdlib_demo.calculate_statistics(data)
    print(f"   Data: {data}")
    print(f"   Mean: {stats['mean']}")
    print(f"   Median: {stats['median']}")
    print(f"   Variance: {stats['variance']}\n")
    
    # 6. Testing fetch_url_data
    print("6. Fetching URL Data:")
    try:
        url = "https://www.example.com"
        byte_count = 100
        data = stdlib_demo.fetch_url_data(url, byte_count)
        print(f"   First {byte_count} bytes from {url}:")
        print(f"   {data}\n")
    except Exception as e:
        print(f"   Error fetching URL: {e}\n")
    
    # 7. Testing get_current_datetime
    print("7. Current Date and Time:")
    datetime_str = stdlib_demo.get_current_datetime()
    print(f"   {datetime_str}\n")
    
    # 8. Testing compress_data
    print("8. Compressing Data:")
    original_data = b"This is a test string to compress. " * 10
    compressed_data = stdlib_demo.compress_data(original_data)
    print(f"   Original size: {len(original_data)} bytes")
    print(f"   Compressed size: {len(compressed_data)} bytes")
    print(f"   Compression ratio: {len(compressed_data) / len(original_data):.2f}\n")
    
    # 9. Testing measure_execution_time
    print("9. Measuring Execution Time:")
    code_str = "[i**2 for i in range(1000)]"
    number = 1000
    execution_time = stdlib_demo.measure_execution_time(code_str, number)
    print(f"   Code: '{code_str}'")
    print(f"   Executions: {number}")
    print(f"   Total time: {execution_time:.6f} seconds")
    print(f"   Average time per execution: {execution_time / number:.9f} seconds\n")


class TestStdlibDemo(unittest.TestCase):
    """Unit tests for the stdlib_demo module."""
    
    def test_get_current_directory(self):
        """Test that get_current_directory returns a non-empty string."""
        result = stdlib_demo.get_current_directory()
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
    
    def test_list_python_files(self):
        """Test that list_python_files returns a list of .py files."""
        current_dir = stdlib_demo.get_current_directory()
        result = stdlib_demo.list_python_files(current_dir)
        self.assertIsInstance(result, list)
        for file in result:
            self.assertTrue(file.endswith('.py'))
    
    def test_get_command_line_args(self):
        """Test that get_command_line_args returns a non-empty list."""
        result = stdlib_demo.get_command_line_args()
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)
    
    def test_find_numbers(self):
        """Test that find_numbers correctly extracts digits."""
        text = "Test 123, another 456 and 789."
        result = stdlib_demo.find_numbers(text)
        self.assertEqual(result, ['123', '456', '789'])
    
    def test_calculate_statistics(self):
        """Test that calculate_statistics returns correct values."""
        data = [1, 2, 3, 4, 5]
        result = stdlib_demo.calculate_statistics(data)
        self.assertEqual(result["mean"], 3.0)
        self.assertEqual(result["median"], 3.0)
        self.assertEqual(result["variance"], 2.5)
    
    def test_compress_data(self):
        """Test that compress_data returns compressed bytes."""
        original = b"Test data" * 100
        compressed = stdlib_demo.compress_data(original)
        self.assertLess(len(compressed), len(original))
    
    def test_get_current_datetime(self):
        """Test that get_current_datetime returns a properly formatted string."""
        result = stdlib_demo.get_current_datetime()
        # Check format YYYY-MM-DD HH:MM:SS
        self.assertRegex(result, r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$')
    
    def test_measure_execution_time(self):
        """Test that measure_execution_time returns a positive float."""
        code = "1 + 1"
        result = stdlib_demo.measure_execution_time(code, 10)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0.0)


if __name__ == "__main__":
    # First demonstrate the functions
    demonstrate_functions()
    
    # Then run unit tests
    print("\n===== RUNNING UNIT TESTS =====\n")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)