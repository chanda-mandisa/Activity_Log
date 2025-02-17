import time
import random
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import winsound
import threading

# Define the log file name
LOG_FILE = "activity_log.txt"

def log_activity(activity):
    """
    Logs the user's activity with a timestamp into the log file.
    :param activity: The activity description provided by the user.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp}: {activity}\n"
    
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)
    
    print(f"Logged: {log_entry.strip()}")  # Debugging print

def play_notification_sound():
    """
    Plays a soft notification sound using a built-in Windows system beep.
    """
    try:
        threading.Thread(target=winsound.MessageBeep, args=(winsound.MB_ICONASTERISK,), daemon=True).start()
    except Exception as e:
        print(f"Sound notification failed: {e}")

def prompt_user():
    """
    Prompts the user to enter their current activity via a fully customized popup window.
    If the user enters a response, it is logged.
    """
    play_notification_sound()  # Alert the user before prompting

    # Create the main popup window
    root = tk.Tk()
    root.title("Activity Logger")
    root.geometry("400x200")  # Ensure proper window size
    root.configure(bg="#f0f0f0")  # Set background color
    root.resizable(False, False)

    # Create a frame for styling
    frame = tk.Frame(root, bg="#f0f0f0")
    frame.pack(pady=20, padx=20)

    # Create a label
    label = tk.Label(frame, text="What are you doing right now?", font=("Arial", 12), bg="#f0f0f0")
    label.pack(pady=5)

    # Create an input field
    entry = ttk.Entry(frame, font=("Arial", 12), width=40)
    entry.pack(pady=5)
    entry.focus_set()
    
    def submit():
        activity = entry.get()
        if activity:
            log_activity(activity)
        root.destroy()
    
    # Bind Enter key to submit function
    entry.bind("<Return>", lambda event: submit())

    # Create a submit button
    submit_btn = ttk.Button(frame, text="OK", command=submit)
    submit_btn.pack(pady=10, side=tk.LEFT, padx=10)

    # Create a cancel button
    cancel_btn = ttk.Button(frame, text="Cancel", command=root.destroy)
    cancel_btn.pack(pady=10, side=tk.RIGHT, padx=10)

    root.mainloop()

def main():
    """
    Runs the activity logger in an infinite loop.
    Prompts the user at three random intervals per hour, spaced at least 10 minutes apart.
    """
    while True:
        # Generate three random wait times, ensuring at least 10 minutes (600 seconds) apart
        start_time = 0
        random_times = []
        for _ in range(3):
            start_time += random.randint(600, 1800)  # Each wait time is between 10-30 minutes
            random_times.append(start_time)

        for wait_time in random_times:
            time.sleep(wait_time)  # Wait for the generated time before prompting
            prompt_user()
        
        print("Completed three prompts for this hour. Restarting...")

if __name__ == "__main__":
    log_activity("DEBUG: Script started.")  # Initial debug log entry
    main()
