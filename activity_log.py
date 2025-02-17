import time
import random
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog
import winsound  # For sound notification (Windows only)

# Log file
log_file = "activity_log.txt"

def log_activity(activity):
    with open(log_file, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}: {activity}\n")

def play_notification_sound():
    # Play a simple beep sound (frequency: 1000 Hz, duration: 500 ms)
    winsound.Beep(1000, 500)

def prompt_user():
    # Play a notification sound
    play_notification_sound()

    # Create a Tkinter window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt the user for input
    activity = simpledialog.askstring("Activity Logger", "What are you doing right now?")

    if activity:
        log_activity(activity)

# Main loop
while True:
    # Generate three random times within the next hour (in seconds)
    random_times = sorted([random.randint(0, 3600 // 3) for _ in range(3)])
    
    for wait_time in random_times:
        time.sleep(wait_time)  # Wait for the random time interval
        prompt_user()
    
    print("Completed three prompts for this hour. Restarting...")
