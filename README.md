# Debian Package Statistics Tool

## Overview  
This Python command-line tool downloads the Debian Contents index file for a specified architecture (e.g. `amd64`, `arm64`), parses the file, and displays the top 10 packages with the most associated files.

## Features  
- **Dynamic Architecture Selection**: Specify an architecture type to download and analyze the corresponding Contents file.  
- **Top 10 Packages by File Count**: Outputs the top 10 packages based on the number of files they contain.  
- **Robust Error Handling**: Handles network and decompression errors gracefully.  
- **Logging**: Logs essential stages of the program for easy debugging.
- **Configurable Logging Levels**: Choose between INFO, DEBUG, or ERROR to control the verbosity of the program output.
- **Code Compliance**: Ensures PEP 8 style compliance using `flake8` and `black`.

## Installation  

### Setting Up the Environment  
It is recommended to set up a virtual environment for this project to isolate dependencies. Follow these steps:

1. Create and activate a virtual environment:
    - **Windows**:
      ```
      python -m venv venv  
      .\venv\Scripts\activate
      ```

    - **Mac/Linux**:
      ```
      python3 -m venv venv  
      source venv/bin/activate
      ```

2. Install the necessary dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage  
Run the tool by specifying your desired architecture (e.g., `amd64`, `arm64`):
```
python package_statistics.py amd64
```

### Configurable Logging Levels
Optionally, the `--log-level` command-line argument allows users to specify the logging level to adjust the verbosity of the output: 
```
python package_statistics.py amd64 --log-level DEBUG
```
- By default, the logging level is set to `INFO` for standard progress messages, but users can switch to `DEBUG` for more detailed output, or `ERROR` for only critical issues. 

## Expected Output  
The tool outputs the package name alongside its file count, ordered from highest to lowest, as well as detailed logs for debugging purposes:  
```
2024-11-04 15:22:19,148 - INFO - Starting the Debian Package Statistics Tool.
2024-11-04 15:22:19,148 - INFO - Parsing command-line arguments.
2024-11-04 15:22:19,150 - INFO - Command-line argument received: architecture=amd64
2024-11-04 15:22:19,151 - INFO - Argument parsing completed in 0.003 seconds.
2024-11-04 15:22:19,151 - INFO - Attempting to download the Contents file from http://ftp.uk.debian.org/debian/dists/stable/main/Contents-amd64.gz
2024-11-04 15:22:20,522 - INFO - Downloaded file size: 11589875 bytes.
2024-11-04 15:22:20,523 - INFO - File successfully downloaded and decompressed.
2024-11-04 15:22:20,523 - INFO - Download and decompression completed in 1.372 seconds.
2024-11-04 15:22:21,937 - INFO - Counting files per package.
2024-11-04 15:22:23,412 - INFO - File counts per package computed successfully.
2024-11-04 15:22:23,413 - INFO - Counting files per package completed in 1.475 seconds.
2024-11-04 15:22:23,414 - INFO - Displaying the top 10 packages by file count.

Top 10 Packages by Number of Files:
devel/piglit                                         53007
science/esys-particle                                18408
math/acl2-books                                      16907
libdevel/libboost1.74-dev,libdevel/libboost1.81-dev  14269
lisp/racket                                           9599
net/zoneminder                                        8161
electronics/horizon-eda                               8130
libdevel/libtorch-dev                                 8089
libdevel/liboce-modeling-dev                          7435
kernel/linux-headers-6.1.0-22-amd64                   6501

2024-11-04 15:22:23,511 - INFO - Displayed the top 10 packages by file count in 0.097 seconds.
2024-11-04 15:22:23,511 - INFO - Processed 34994 packages in total.
2024-11-04 15:22:23,511 - INFO - Total process completed in 4.363 seconds.
```

## Code Linting and Formatting  
These commands can be used to format and lint the code, in order to verify the compliancy of the code:   

1. Format with `black` (to auto-format the code):  
    ```
    black package_statistics.py  
    ```

    ```
    Expected output:
    All done! ✨ 🍰 ✨  
    1 file left unchanged.
    ```

2. Lint with `flake8` (to catch any remaining issues that black hasn't handled):  
    ```
    flake8 package_statistics.py  
    ```

    ```
    Expected output:
    package_statistics.py:21:80: E501 line too long (82 > 79 characters)
    package_statistics.py:42:80: E501 line too long (82 > 79 characters)
    package_statistics.py:54:80: E501 line too long (84 > 79 characters)
    package_statistics.py:58:80: E501 line too long (85 > 79 characters)
    package_statistics.py:60:80: E501 line too long (80 > 79 characters)
    package_statistics.py:78:80: E501 line too long (87 > 79 characters)
    package_statistics.py:92:80: E501 line too long (84 > 79 characters)
    package_statistics.py:93:80: E501 line too long (82 > 79 characters)
    package_statistics.py:96:80: E501 line too long (98 > 79 characters)
    package_statistics.py:133:80: E501 line too long (90 > 79 characters)
    package_statistics.py:149:80: E501 line too long (86 > 79 characters)
    package_statistics.py:150:80: E501 line too long (84 > 79 characters)
    package_statistics.py:166:80: E501 line too long (102 > 79 characters)
    package_statistics.py:184:80: E501 line too long (85 > 79 characters)
    package_statistics.py:194:80: E501 line too long (85 > 79 characters)  
    ```

   These line-length warnings are considered acceptable as they align with the intended use cases for `flake8`.

## Testing
To verify the core functionality of the tool, unit tests are provided for key functions. Run these tests using `unittest` with the `-v` (verbose) option:
```
python -m unittest -v test_package_statistics.py
```

### Expected Output:
You should see output like the following:
```
test_count_files_empty_input (test_package_statistics.TestPackageStatistics) ... 
--------------------------------------------------
2024-11-01 19:55:00,958 - INFO - Counting files per package.
2024-11-01 19:55:00,959 - INFO - File counts per package computed successfully.
2024-11-01 19:55:00,959 - INFO - Counting files per package completed in 0.000 seconds.
Log output: No additional log messages. Test ran successfully.


ok
test_count_files_per_package (test_package_statistics.TestPackageStatistics) ...
--------------------------------------------------
2024-11-01 19:55:00,961 - INFO - Counting files per package.
2024-11-01 19:55:00,961 - INFO - File counts per package computed successfully.
2024-11-01 19:55:00,961 - INFO - Counting files per package completed in 0.000 seconds.
Log output: No additional log messages. Test ran successfully.


ok
test_count_files_single_line_multiple_packages (test_package_statistics.TestPackageStatistics) ...
--------------------------------------------------
2024-11-01 19:55:00,962 - INFO - Counting files per package.
2024-11-01 19:55:00,963 - INFO - File counts per package computed successfully.
2024-11-01 19:55:00,963 - INFO - Counting files per package completed in 0.001 seconds.
Log output: No additional log messages. Test ran successfully.


ok
test_display_top_packages (test_package_statistics.TestPackageStatistics) ...
--------------------------------------------------
2024-11-01 19:55:00,964 - INFO - Displaying the top 2 packages by file count.
2024-11-01 19:55:00,965 - INFO - Displayed the top 2 packages by file count in 0.000 seconds.
Log output: No additional log messages. Test ran successfully.


ok
test_parse_arguments_invalid_architecture (test_package_statistics.TestPackageStatistics) ...
--------------------------------------------------
2024-11-01 19:55:00,966 - INFO - Parsing command-line arguments.
2024-11-01 19:55:00,968 - ERROR - Unsupported architecture specified: example_invalid_arch. Supported types are: amd64, armhf, s390x, mipsel, all, armel, mips64el, arm64, ppc64el, i386
2024-11-01 19:55:00,968 - INFO - Argument parsing completed in 0.003 seconds.
Log output: No additional log messages. Test ran successfully.


ok
test_parse_arguments_valid_architecture (test_package_statistics.TestPackageStatistics) ...
--------------------------------------------------
2024-11-01 19:55:00,969 - INFO - Parsing command-line arguments.
2024-11-01 19:55:00,972 - INFO - Command-line argument received: architecture=amd64
2024-11-01 19:55:00,972 - INFO - Argument parsing completed in 0.002 seconds.
Log output: No additional log messages. Test ran successfully.


ok

----------------------------------------------------------------------
Ran 6 tests in 0.019s

OK
```

These tests confirm that the tested functions are working correctly (e.g. `count_files_per_package` accurately counts files associated with each package and `display_top_packages` correctly displays the top packages based on file count).

## Deactivating the Virtual Environment
To deactivate the virtual environment after you’re finished, simply run:
```
deactivate
```

## Design Decisions  
- **File Handling**: The `.gz` file is decompressed directly in memory to avoid file I/O and enhance performance.  
- **Error Handling**: The program handles potential download and decompression errors, logging them and exiting instead of crashing.
- **Logging**: Logs essential stages of the program for easy debugging.
- **Configurable Logging Levels**: Choose between different logging levels (e.g., INFO, DEBUG) to control output verbosity.
- **Code Compliance**: Ensures PEP 8 style compliance using `flake8` and `black`.

## Supported Architectures

The tool supports the following architectures:
- `amd64`, `arm64`, `armel`, `armhf`, `i386`, `mips64el`, `mipsel`, `ppc64el`, `s390x`, and `all`.

### Note on Architecture Support
- **Main Architectures**: The tool covers all primary binary architectures listed above.
- **`all` Variant**: This variant includes combined contents for all architectures, providing a universal view.
- **Excluded Variants**: The tool intentionally excludes `source` and `udeb` variants:
  - **`source`**: This file contains source packages, which are different from binary packages and may not fit the analysis focus of this tool.
  - **`udeb` Variants**: These are minimal versions of Debian packages used specifically for installation and bootstrapping, and are not relevant for the regular package contents analysis.

## Future Improvements

Potential areas for enhancing the tool include:
1. **Additional Architecture Support**: Extend support to include `source` and `udeb` variants, providing options to analyze source packages and minimal installer packages. This would require modifications to filter content based on package types.
2. **Parallel Processing**: For large files, implement parallel processing to speed up file counting and analysis, particularly beneficial when dealing with high file counts (e.g. in architectures like `all`). Approaches include Python's concurrent.futures (cost-effective, best for smaller data) or AWS Lambda/S3 (highly scalable, ideal for large data volumes).
3. **Configurable Output**: Add options for configurable output formats (e.g., JSON or CSV) to make it easier to integrate with other tools or workflows.
4. **Docker Setup**: Create a Dockerfile for containerized execution, ensuring that dependencies and environments are consistent regardless of the user’s system setup.
5. **Enhanced Logging Options**: Add more granular logging levels or a customizable log format to better cater to different user needs and use cases.


## Development Time  
Approximately 3-4 hours were spent designing, implementing, testing, and refining the tool. This was a fun project.
