"""
log_analyzer_v2.py

Advanced log file analyzer with filtering options by log level, keyword, and date.
Generates detailed reports and visualizations.

Author: Your Name
Date: 2025-10-26
"""

import os
import argparse
import matplotlib.pyplot as plt
import re
from datetime import datetime

# -------------------------------
# Functions
# -------------------------------

def read_log(file_path):
    """Read the log file and return its content as a list of lines."""
    with open(file_path, 'r') as f:
        return f.readlines()

def filter_logs(log_lines, level=None, keyword=None, start_date=None, end_date=None, date_format="%Y-%m-%d"):
    """
    Filter logs by level, keyword, or date range.
    level: "ERROR", "WARNING", "INFO", etc.
    keyword: string to search in log lines
    start_date, end_date: filter logs within a date range (YYYY-MM-DD)
    """
    filtered = []
    
    for line in log_lines:
        match_level = True
        match_keyword = True
        match_date = True
        
        if level and level not in line:
            match_level = False
        
        if keyword and keyword.lower() not in line.lower():
            match_keyword = False
        
        if start_date or end_date:
            # Extract date from line (assuming date at start of line, adjust regex as needed)
            date_match = re.match(r"(\d{4}-\d{2}-\d{2})", line)
            if date_match:
                log_date = datetime.strptime(date_match.group(1), date_format)
                if start_date and log_date < start_date:
                    match_date = False
                if end_date and log_date > end_date:
                    match_date = False
            else:
                match_date = False
        
        if match_level and match_keyword and match_date:
            filtered.append(line.strip())
    
    return filtered

def generate_report(filtered_logs, output_dir="output"):
    """Generate a detailed report from filtered logs."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    report_path = os.path.join(output_dir, "filtered_report.txt")
    with open(report_path, "w") as f:
        f.write(f"Total Entries: {len(filtered_logs)}\n\n")
        for line in filtered_logs:
            f.write(f"{line}\n")
    
    print(f"Filtered report saved to {report_path}")

def plot_summary(filtered_logs, output_dir="output"):
    """Generate visualization of log levels in filtered logs."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    levels = ["ERROR", "WARNING", "INFO", "DEBUG"]
    counts = [sum(1 for line in filtered_logs if lvl in line) for lvl in levels]
    
    plt.bar(levels, counts, color=['red', 'orange', 'blue', 'green'])
    plt.title("Log Level Summary")
    plt.ylabel("Count")
    
    plot_path = os.path.join(output_dir, "filtered_visualization.png")
    plt.savefig(plot_path)
    plt.show()
    print(f"Visualization saved to {plot_path}")

# -------------------------------
# Main Execution
# -------------------------------

def main():
    parser = argparse.ArgumentParser(description="Advanced Log File Analyzer with filters.")
    parser.add_argument("logfile", help="Path to the log file to analyze")
    parser.add_argument("--level", help="Filter by log level (ERROR, WARNING, INFO, DEBUG)")
    parser.add_argument("--keyword", help="Filter by keyword in logs")
    parser.add_argument("--start", help="Start date filter (YYYY-MM-DD)")
    parser.add_argument("--end", help="End date filter (YYYY-MM-DD)")
    
    args = parser.parse_args()
    
    log_file = args.logfile
    if not os.path.exists(log_file):
        print(f"Log file {log_file} not found!")
        return
    
    lines = read_log(log_file)
    
    start_date = datetime.strptime(args.start, "%Y-%m-%d") if args.start else None
    end_date = datetime.strptime(args.end, "%Y-%m-%d") if args.end else None
    
    filtered_logs = filter_logs(lines, level=args.level, keyword=args.keyword, start_date=start_date, end_date=end_date)
    
    print(f"Total Filtered Entries: {len(filtered_logs)}")
    
    generate_report(filtered_logs)
    plot_summary(filtered_logs)

if __name__ == "__main__":
    main()
