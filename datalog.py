import csv
from datetime import datetime
import os

def write_log_to_csv(shape, color):
    """
    Writes a log entry containing the detected shape, color, and the current timestamp 
    to a CSV file named 'log.csv'. If the file does not exist or is empty, it adds a header.

    Args:
        shape (str): The detected shape (e.g., 'circle', 'square', etc.).
        color (str): The detected color (e.g., 'red', 'blue', etc.).

    Returns:
        None
    """
    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Prepare the log entry
    log_entry = [timestamp, shape, color]

    # Open the CSV file in append mode
    with open("log.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # If the file is empty, write the header
        if file.tell() == 0:
            writer.writerow(['Timestamp', 'Shape', 'Color'])

        # Write the log entry
        writer.writerow(log_entry)