# Activity Checklist

Activity Checklist is a lightweight Python script that prompts users every 15 minutes to log their current activities. It is designed to enhance productivity tracking, self-awareness, and time management.

## Features

- **Automated Activity Prompts**: The script runs in the background and prompts users every 15 minutes (on the hour, 15, 30, and 45-minute marks).
- **Modernized Tkinter GUI**: A simple, fullscreen GUI for seamless activity tracking.
- **Prevents Duplicate Instances**: Ensures that only one instance of the script is running at any time.
- **Timestamped Logging**: Saves selected activities in `activity_checklist_log.txt` for easy reference and analysis.
- **Lightweight and Efficient**: Runs with minimal resource consumption.

## Getting Started

This script allows users to track their activities at regular intervals, helping them maintain focus and build better time management habits.

### Installation

#### Clone the Repository

```sh
git clone https://github.com/chanda-mandisa/Activity_Checklist.git
cd Activity_Checklist
```

### Running the Script

Run the script using:

```sh
python activity_checklist.py
```

### System Requirements

- **Python 3.x**
- **Tkinter** (Included in most Python distributions)
- **psutil** (For process management; install using `pip install psutil` if not already available)

## Usage

- Once started, the script will prompt you every 15 minutes with a fullscreen checklist.
- Select one or more activities you are currently engaged in (Research, Writing, Coding, Reading, Break, or Other).
- Click "Submit," and the selected activities will be saved to `activity_checklist_log.txt` with a timestamp.
- The log file records all activity selections for productivity tracking.

## Customization

- Modify the script to adjust the prompt frequency (default: every 15 minutes).
- Add or remove activity options in the `TASKS` list.
- Change the logging format or add additional metadata as needed.

## Troubleshooting

### Common Issues

#### Script not starting
- Ensure Python is installed and the correct script is executed.
- Check if another instance is already running.

#### Logs not saving
- Verify that the `activity_checklist_log.txt` file is writable.
- Ensure the script has necessary file permissions.

#### GUI not appearing
- Make sure Tkinter is installed and functional on your system.
- If running on a headless server, consider disabling the GUI and using a CLI-based approach.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Contributions

Contributions are welcome! Feel free to submit a pull request or report issues.

## Author
Developed by [chanda-mandisa].


