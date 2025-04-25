# LAB 11

## Overview
In this assignment, you will create a module named `stdlib_demo.py` that demonstrates various functionalities of the Python Standard Library. Each function in this module must follow the specifications below, with clear details on the input types and expected outputs to facilitate unit testing. Additionally, you will create a `main.py` file that shows how to call and test these functions.

## Project Structure
- **stdlib_demo.py** – Contains all the functions required for the assignment.
- **main.py** – Demonstrates the usage of the functions in `stdlib_demo.py` and may include basic tests.

---

## Assignment Tasks

### 1. Function: `get_current_directory() -> str`
- **Purpose:** Retrieve the current working directory.
- **Inputs:** 
  - No parameters.
- **Output:** 
  - A string representing the current working directory (as returned by `os.getcwd()`).


---

### 2. Function: `list_python_files(directory: str) -> list`
- **Purpose:** List all Python files in the specified directory.
- **Inputs:** 
  - `directory` (str): The path to the directory in which to search for files.
- **Output:** 
  - A list of strings, where each string is the name of a file ending with `.py`.


---

### 3. Function: `get_command_line_args() -> list`
- **Purpose:** Retrieve the command-line arguments.
- **Inputs:** 
  - No parameters.
- **Output:** 
  - A list of strings representing the command-line arguments (using `sys.argv`).


---

### 4. Function: `find_numbers(text: str) -> list`
- **Purpose:** Extract all sequences of digits (numbers) from the given text.
- **Inputs:** 
  - `text` (str): The string to search for number sequences.
- **Output:** 
  - A list of strings, each representing a sequence of digits found in the text.


---

### 5. Function: `calculate_statistics(data: list) -> dict`
- **Purpose:** Compute basic statistical measures from a list of numbers.
- **Inputs:** 
  - `data` (list): A list of numbers (integers or floats).
- **Output:** 
  - A dictionary with the following keys:
    - `"mean"`: The arithmetic mean.
    - `"median"`: The median value.
    - `"variance"`: The variance.


---

### 6. Function: `fetch_url_data(url: str, byte_count: int) -> bytes`
- **Purpose:** Retrieve a specified number of bytes from the given URL.
- **Inputs:** 
  - `url` (str): The URL from which to fetch data.
  - `byte_count` (int): The number of bytes to read from the URL.
- **Output:** 
  - A bytes object containing the fetched data.


---

### 7. Function: `get_current_datetime() -> str`
- **Purpose:** Get the current date and time as a formatted string.
- **Inputs:** 
  - No parameters.
- **Output:** 
  - A string formatted as `"YYYY-MM-DD HH:MM:SS"`, representing the current date and time.

---

### 8. Function: `compress_data(data: bytes) -> bytes`
- **Purpose:** Compress the provided data using the gzip algorithm.
- **Inputs:** 
  - `data` (bytes): A bytes object to compress.
- **Output:** 
  - A bytes object representing the compressed data.


---

### 9. Function: `measure_execution_time(code_str: str, number: int) -> float`
- **Purpose:** Measure the execution time of a code snippet.
- **Inputs:** 
  - `code_str` (str): A string containing the code to execute.
  - `number` (int): The number of times the code snippet should be executed.
- **Output:** 
  - A float representing the total execution time (in seconds).


---

## Additional Instructions
- **Code Quality:** Ensure that your code is well-commented, follows Python best practices, and uses appropriate error handling.
- **Imports:** Your `stdlib_demo.py` must import only standard library modules required for each function.
- **Testing:** In `main.py`, include sample calls to each function with example inputs and print the results. You may also include unit tests using Python’s `unittest` module to validate your implementation.

