import tkinter as tk
import os
import time
import psutil
from datetime import datetime

# ---------------------- CONFIGURATION ---------------------- #
# Define a directory for logging user activity
LOG_DIR = os.path.expanduser("~/activity_log")
LOG_FILE = os.path.join(LOG_DIR, "activity_checklist_log.txt")

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# List of tasks user can select from
TASKS = ["Research", "Writing", "Coding", "Reading", "Break", "Other"]

# ---------------------- PROCESS CHECK ---------------------- #
def is_already_running():
    """
    Prevents multiple instances of this script from running at the same time.
    This is useful to avoid duplicate popups or redundant processes.
    """
    current_pid = os.getpid()
    script_name = os.path.basename(__file__)

    for process in psutil.process_iter(attrs=['pid', 'cmdline']):
        try:
            if process.info['cmdline'] and script_name in process.info['cmdline'][0] and process.info['pid'] != current_pid:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False

# ---------------------- ACTIVITY LOGGING ---------------------- #
def save_log(selections):
    """
    Logs the selected tasks with a timestamp.
    The log file stores historical data for activity tracking.
    """
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {', '.join(selections)}\n")

# ---------------------- CHECKLIST POPUP ---------------------- #
def open_checklist():
    """
    Opens a checklist GUI where users can select what they are currently working on.
    This uses Tkinter to create a simple fullscreen interface.
    """
    root = tk.Tk()
    root.title("Activity Checklist")
    root.attributes('-fullscreen', True)  # Opens in fullscreen mode

    tk.Label(root, text="Select what you're working on:", font=("Arial", 16)).pack(pady=20)

    check_vars = {task: tk.IntVar() for task in TASKS}

    for task, var in check_vars.items():
        tk.Checkbutton(root, text=task, variable=var, font=("Arial", 14)).pack(anchor="w", padx=50, pady=5)

    def submit():
        """Saves the selected tasks and closes the checklist window."""
        selected_tasks = [task for task, var in check_vars.items() if var.get()]
        save_log(selected_tasks)
        root.destroy()

    tk.Button(root, text="Submit", command=submit, font=("Arial", 16), padx=20, pady=10).pack(pady=30)

    root.mainloop()

# ---------------------- CHECKLIST SCHEDULER ---------------------- #
def schedule_checklist():
    """
    Schedules the checklist popup every 15 minutes (at 00, 15, 30, 45 minutes).
    Ensures only one instance of the script runs at any given time.
    """
    if is_already_running():
        print("Another instance is already running. Exiting.")
        return

    while True:
        now = datetime.now()
        next_minute = ((now.minute // 15) + 1) * 15  # Round to nearest 15-minute mark
        if next_minute >= 60:
            next_minute = 0
            wait_time = (60 - now.minute) * 60 - now.second
        else:
            wait_time = (next_minute - now.minute) * 60 - now.second

        print(f"Next checklist prompt in {wait_time} seconds.")
        time.sleep(wait_time)
        open_checklist()

# ---------------------- SCRIPT ENTRY POINT ---------------------- #
if __name__ == "__main__":
    schedule_checklist()

