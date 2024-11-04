"""
Debian Package Statistics Tool

This tool downloads the Debian Contents file for a specified architecture,
parses it, and displays the top 10 packages with the most associated files.
"""

import argparse
import requests
import gzip
from io import BytesIO
from collections import defaultdict
import logging
import time

# Setting up logging to capture debugging information
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Supported architectures include main binary types and "all" for a combined view.
# Excludes "source" and "udeb" types due to their specialized use cases.
SUPPORTED_ARCHITECTURES = {
    "amd64",
    "arm64",
    "armel",
    "armhf",
    "i386",
    "mips64el",
    "mipsel",
    "ppc64el",
    "s390x",
    "all",
}


def parse_arguments():
    """Parse command-line arguments to capture the architecture type and logging level."""
    start_time = time.time()  # Start timer for the argument parsing
    logging.info("Parsing command-line arguments.")

    parser = argparse.ArgumentParser(description="Debian Package Statistics Tool")
    parser.add_argument(
        "architecture", type=str, help="Architecture type (e.g., amd64, arm64)"
    )
    parser.add_argument(
        "--log-level",
        type=str,
        choices=["DEBUG", "INFO", "ERROR"],
        default="INFO",  # Defaulting to INFO level if not provided
        help="Set the logging level (default: INFO)",
    )
    
    args = parser.parse_args()

    # Setting the logging level based on the command-line argument
    logging.getLogger().setLevel(logging.getLevelName(args.log_level))

    if args.architecture not in SUPPORTED_ARCHITECTURES:
        logging.error(
            f"Unsupported architecture specified: {args.architecture}. "
            f"Supported types are: {', '.join(SUPPORTED_ARCHITECTURES)}"
        )
        logging.info(
            f"Argument parsing completed in {time.time() - start_time:.3f} seconds."
        )
        exit(1)  # Exiting early with an error status

    logging.info(f"Command-line argument received: architecture={args.architecture}")
    logging.info(
        f"Argument parsing completed in {time.time() - start_time:.3f} seconds."
    )
    return args



def download_contents_file(architecture):
    """
    Downloads and decompresses the Contents file for the given architecture
    from the Debian mirror.

    Parameters:
        architecture (str): The architecture type (e.g., amd64, arm64).

    Returns:
        list of str: Lines from the decompressed Contents file, or None if
        download fails.
    """
    url = (
        f"http://ftp.uk.debian.org/debian/dists/stable/main/Contents-{architecture}.gz"
    )
    logging.info(f"Attempting to download the Contents file from {url}")

    start_time = time.time()  # Starting timer for the download

    try:
        # Attempting to download the compressed file from the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raising error for bad status codes

        # Logging the size of the downloaded content
        logging.info(f"Downloaded file size: {len(response.content)} bytes.")

        # Decompressing file content in memory and reading lines with utf-8 encoding
        with gzip.open(BytesIO(response.content), "rt", encoding="utf-8") as file:
            logging.info("File successfully downloaded and decompressed.")
            logging.info(
                f"Download and decompression completed in {time.time() - start_time:.3f} seconds."
            )
            return file.readlines()

    except requests.exceptions.RequestException as e:
        logging.error(f"Error downloading file: {e}")
        return None
    except gzip.BadGzipFile as e:
        logging.error(f"Error decompressing file: {e}")
        return None


def count_files_per_package(lines):
    """
    Counts the number of files associated with each package in the Contents
    file.

    Parameters:
        lines (list of str): Lines from the Contents file.

    Returns:
        dict: Dictionary with package names as keys and file counts as values.
    """
    logging.info("Counting files per package.")
    start_time = time.time()  # Starting timer for the counting process
    package_counts = defaultdict(int)  # Default value for each package is 0
    for line in lines:
        parts = line.split()  # Splitting the line into file path and packages

        # Ensuring we have both a path and packages
        if len(parts) > 1:
            packages = parts[1:]  # Skipping the file path, keep package names
            for package in packages:
                package_counts[package] += 1  # Incremental file count

    logging.info("File counts per package computed successfully.")
    logging.info(
        f"Counting files per package completed in {time.time() - start_time:.3f} seconds."
    )
    return package_counts


def display_top_packages(package_counts, top_n=10):
    """
    Sorts and displays the top N packages by file count.

    Parameters:
        package_counts (dict): Dictionary of package file counts.
        top_n (int): Number of top packages to display.
    """
    logging.info(f"Displaying the top {top_n} packages by file count.")
    start_time = time.time()  # Starting timer for the display process

    # Sorting packages by file count in descending order and getting the top N entries
    top_packages = sorted(package_counts.items(), key=lambda x: x[1], reverse=True)[
        :top_n
    ]

    # Determining the maximum width for the package column for better alignment
    max_package_length = max(len(package) for package, _ in top_packages)

    # Printing the results in a readable format with aligned columns
    print("\nTop 10 Packages by Number of Files:")
    for package, count in top_packages:
        print(f"{package.ljust(max_package_length)} {count:>6}")

    # Adding a new line after the printed output for better readability
    print()

    logging.info(
        f"Displayed the top {top_n} packages by file count in {time.time() - start_time:.3f} seconds."
    )


def main():
    """Main function that orchestrates the downloading, parsing, and displaying
    of package data."""
    logging.info("Starting the Debian Package Statistics Tool.")
    overall_start_time = time.time()  # Starting timer for the entire process

    args = parse_arguments()  # Capturing the architecture argument

    lines = download_contents_file(
        args.architecture
    )  # Downloading and decompressing the Contents file

    # Proceeding only if the download was successful
    if lines:
        package_counts = count_files_per_package(lines)  # Counting files per package
        display_top_packages(
            package_counts
        )  # Displaying the top 10 packages by file count
        logging.info(f"Processed {len(package_counts)} packages in total.")
    else:
        logging.error("No data to process. Exiting program.")

    # Logging the total time taken for the process
    logging.info(
        f"Total process completed in {time.time() - overall_start_time:.3f} seconds."
    )


if __name__ == "__main__":
    main()
