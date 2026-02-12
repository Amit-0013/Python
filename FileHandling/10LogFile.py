##Write a function that creates a log file named `activity.log` and writes log messages with timestamps.
import datetime
def log_message(msg , filename = 'sample.txt'):
    timestamp = datetime.datetime.now().isoformat()
    with open(filename,'w') as file:
        file.write(f"{msg} {timestamp}")
log_message("Hello the current time stamp is: ")