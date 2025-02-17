# Activity Logger

Activity Logger is a lightweight Python script that prompts users at random intervals to log their current activities. It is designed to help with productivity tracking and self-awareness.

## Features
- Prompts the user three times per hour, ensuring at least 10-minute intervals.
- Uses a modernized Tkinter GUI for user input.
- Logs activities to `activity_log.txt` with timestamps.
- Runs automatically in the background.

## Getting Started
This script allows users to track their activities through periodic prompts, helping to improve self-awareness and time management.

## Installation
### Clone the Repository
```sh
git clone https://github.com/chanda-mandisa/Activity_Log.git
cd Activity_Log
```

### Running the Script
Run the script using:
```sh
python activity_log.py
```

## System Requirements
- **Python 3.x**
- **Tkinter (included in most Python distributions)**

## Usage
- Once started, the script will prompt you to log your activity at intervals of at least 10 minutes.
- You can enter what you're doing in the prompt, and it will be saved to `activity_log.txt`.
- The log file will contain timestamps to help track patterns over time.

## Customization
- Modify the script to adjust the number of prompts per hour.
- Change the logging format or add additional metadata as needed.

## Troubleshooting
### Common Issues
- **Script not starting**: Ensure Python is installed and the correct script is executed.
- **Logs not saving**: Check permissions for writing to `activity_log.txt`.
- **GUI not appearing**: Ensure Tkinter is installed and functional on your system.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Contributions
Contributions are welcome! Feel free to submit a pull request or report issues.

## Author
Developed by [chanda-mandisa].
