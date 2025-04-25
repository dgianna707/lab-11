import os
import sys
import re
import statistics
import urllib.request
import datetime
import gzip
import timeit
from typing import List, Dict, Union


def get_current_directory() -> str:
    """
    Retrieve the current working directory.
    
    Returns:
        str: A string representing the current working directory.
    """
    try:
        return os.getcwd()
    except OSError as e:
        print(f"Error getting current directory: {e}")
        return ""


def list_python_files(directory: str) -> List[str]:
    """
    List all Python files in the specified directory.
    
    Args:
        directory (str): The path to the directory in which to search for files.
    
    Returns:
        list: A list of strings, where each string is the name of a file ending with '.py'.
    """
    try:
        # Ensure the directory exists
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")
        
        # List all files in the directory and filter for .py extension
        return [file for file in os.listdir(directory) if file.endswith('.py')]
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error listing Python files: {e}")
        return []


def get_command_line_args() -> List[str]:
    """
    Retrieve the command-line arguments.
    
    Returns:
        list: A list of strings representing the command-line arguments.
    """
    return sys.argv


def find_numbers(text: str) -> List[str]:
    """
    Extract all sequences of digits (numbers) from the given text.
    
    Args:
        text (str): The string to search for number sequences.
    
    Returns:
        list: A list of strings, each representing a sequence of digits found in the text.
    """
    if not isinstance(text, str):
        print("Input must be a string")
        return []
    
    # Use regex pattern to find all digit sequences
    pattern = r'\d+'
    return re.findall(pattern, text)


def calculate_statistics(data: List[Union[int, float]]) -> Dict[str, float]:
    """
    Compute basic statistical measures from a list of numbers.
    
    Args:
        data (list): A list of numbers (integers or floats).
    
    Returns:
        dict: A dictionary with keys 'mean', 'median', and 'variance'.
    """
    try:
        if not data:
            raise ValueError("Input list is empty")
        
        # Calculate statistics using the statistics module
        mean = statistics.mean(data)
        median = statistics.median(data)
        variance = statistics.variance(data)
        
        return {
            "mean": mean,
            "median": median,
            "variance": variance
        }
    except (TypeError, ValueError) as e:
        print(f"Error calculating statistics: {e}")
        return {"mean": 0.0, "median": 0.0, "variance": 0.0}


def fetch_url_data(url: str, byte_count: int) -> bytes:
    """
    Retrieve a specified number of bytes from the given URL.
    
    Args:
        url (str): The URL from which to fetch data.
        byte_count (int): The number of bytes to read from the URL.
    
    Returns:
        bytes: A bytes object containing the fetched data.
    """
    try:
        with urllib.request.urlopen(url) as response:
            return response.read(byte_count)
    except (urllib.error.URLError, ValueError) as e:
        print(f"Error fetching URL data: {e}")
        return b''


def get_current_datetime() -> str:
    """
    Get the current date and time as a formatted string.
    
    Returns:
        str: A string formatted as "YYYY-MM-DD HH:MM:SS", representing the current date and time.
    """
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime("%Y-%m-%d %H:%M:%S")


def compress_data(data: bytes) -> bytes:
    """
    Compress the provided data using the gzip algorithm.
    
    Args:
        data (bytes): A bytes object to compress.
    
    Returns:
        bytes: A bytes object representing the compressed data.
    """
    try:
        return gzip.compress(data)
    except (TypeError, ValueError) as e:
        print(f"Error compressing data: {e}")
        return b''


def measure_execution_time(code_str: str, number: int) -> float:
    """
    Measure the execution time of a code snippet.
    
    Args:
        code_str (str): A string containing the code to execute.
        number (int): The number of times the code snippet should be executed.
    
    Returns:
        float: A float representing the total execution time (in seconds).
    """
    try:
        # Using timeit to measure execution time
        return timeit.timeit(code_str, number=number)
    except (SyntaxError, NameError) as e:
        print(f"Error measuring execution time: {e}")
        return 0.0