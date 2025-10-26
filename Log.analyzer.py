For log_analyzer.py


1. Header/Docstring
"""
log_analyzer.py

A Python script to analyze log files, detect errors, and generate summary reports.
Author: Your Name
Date: 2025-10-26
"""


---

2. Imports

Include necessary libraries, e.g.:

import os
import re
import matplotlib.pyplot as plt


---

3. Functions (Modular Approach)

Break your code into functions for readability and reuse:

def read_log(file_path):
    """Read the log file and return its content as a list of lines."""
    with open(file_path, 'r') as f:
        return f.readlines()

def parse_logs(log_lines):
    """Parse logs to extract useful information (e.g., errors, warnings)."""
    errors = []
    warnings = []
    for line in log_lines:
        if "ERROR" in line:
            errors.append(line)
        elif "WARNING" in line:
            warnings.append(line)
    return errors, warnings

def generate_report(errors, warnings):
    """Print summary report."""
    print(f"Total Errors: {len(errors)}")
    print(f"Total Warnings: {len(warnings)}")
    # Optionally save to a file
    with open("output/report.txt", "w") as f:
        f.write(f"Total Errors: {len(errors)}\n")
        f.write(f"Total Warnings: {len(warnings)}\n")

def plot_summary(errors, warnings):
    """Generate a simple visualization of errors vs warnings."""
    plt.bar(['Errors', 'Warnings'], [len(errors), len(warnings)], color=['red', 'orange'])
    plt.title('Log Summary')
    plt.savefig("output/visualization.png")
    plt.show()


---

4. Main Execution Block

So users can run it as a script:

if __name__ == "__main__":
    log_file = "sample_logs/test.log"
    
    if not os.path.exists(log_file):
        print(f"Log file {log_file} not found!")
        exit(1)
    
    lines = read_log(log_file)
    errors, warnings = parse_logs(lines)
    generate_report(errors, warnings)
    plot_summary(errors, warnings)


---

5. Optional Enhancements

Command-line arguments using argparse to allow users to specify any log file.

Filtering by date or log level.

Multiple output formats (CSV, PDF).




