from datetime import datetime
import os

LOG_PATH = "data/user_logs.txt"

def log_action(action, log_file=LOG_PATH):
    """Append a user action with a timestamp to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(f"[{timestamp}] {action}\n")

def search_logs(keyword, log_file=LOG_PATH):
    """Search the log file for lines that match a keyword."""
    try:
        with open(log_file, "r") as file:
            for line in file:
                if keyword in line:
                    print(line.strip())
    except FileNotFoundError:
        print("Log file not found.") 

# Each time I run script these actions will be logged to the file user_logs.txt
log_action("User logged in")
log_action("User updated profile")

# Search the logs for any actions containing the keyword "User"
search_logs("User")
# Search the logs for any actions containing the keyword "profile"
search_logs("profile")
# Test try except block by searching for a keyword that doesn't exist
search_logs("User", "data/poo_logs.txt")