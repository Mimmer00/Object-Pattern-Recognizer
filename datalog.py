

import csv
from datetime import datetime

# function to write data into CSV file    
def write_log_to_csv(file_name, shape, color):
    #timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # entries
    log_entry = [timestamp, shape, color]

    # open file
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # check if row is empty
        if file.tell() == 0:
            writer.writerow(['Timestamp', 'Shape', 'Color'])

        
        writer.writerow(log_entry)


# write_log_to_csv('log.csv', 'Circle', 'Red')

