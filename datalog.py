

import csv
from datetime import datetime
import os

   
def write_log_to_csv(shape, color):
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    
    log_entry = [timestamp, shape, color]

    
    with open("log.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        
        
        if file.tell() == 0:
            writer.writerow(['Timestamp', 'Shape', 'Color'])

        
        writer.writerow(log_entry)



