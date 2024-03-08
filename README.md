# MOTD (Message of the Day) Python Class

## Overview
The MOTD Python Class is a lightweight and easily pluggable solution for adding messages to any Python project. This class reads messages from text files and provides a method to randomly select and retrieve a message for display as the Message of the Day (MOTD).

## Features
- Provides a simple interface for fetching motivational or demotivational messages.
- Messages are stored in text files, making it easy to add or modify messages.
- Lightweight and suitable for integration into any Python project.
- Promotes a humorous and lighthearted atmosphere by adding motivational or demotivational elements.

## Usage
1. Clone or download the repository to your local machine.
2. Copy the `motd.py` file into your Python project directory.
3. Ensure that the text files containing messages are located in the specified file path (`data/` by default).
4. Import the `MOTD` class into your Python script.
5. Create an instance of the `MOTD` class.
6. Call the appropriate method to retrieve or set messages.

Example usage:
```python
from motd import MOTD

# Create an instance of the MOTD class (default file_path is "data/")
motd = MOTD()

# Retrieve and display a random message from a text file in the data folder
print("Today's message: ", motd.get_random_message_from_catalogue())
```
Alternatively, to set a specific message:
```python
# Set a specific message
motd.set_message("Have a great day!")

# Retrieve and display the set message
print("Today's message: ", motd.get_message())
```

## Text Files
You can create your own text files with messages. Each line in the text file will be treated as a separate message and read as a string by the MOTD Python class. Simply ensure that the text file is located in the `data/` folder within your project directory, and the MOTD class will automatically recognize it.
- `proved_wrong_quotes.txt`: Contains famous quotes by individuals that were later proven wrong.
- `demotivational.txt`: Contains demotivational messages to be displayed as MOTD.


## Planned Functions
- `get_all_messages_from_file`: Returns a list of all messages from a specific file.
- `get_all_messages_from_catalogue`: Returns a list of all available files and their messages.
- `add_message_to_file`: Adds a new message to a specified file.
- `remove_message_from_file`: Removes a specific message from a file.
- `clear_messages_from_file`: Clears all messages from a specified file.
- `update_message_in_file`: Updates a message in a specified file with a new one.

## License
This project is licensed under the Creative Commons Attribution 4.0 International License. You are free to use, share, and modify the code and messages, provided that you give appropriate credit to the original source.

## Contribution
Contributions to this project are welcome! If you have suggestions for new messages or improvements to the code, feel free to submit a pull request.

## Disclaimer
While this MOTD (Message of the Day) Python class embraces a dark sense of humor with a hint of self-deprecation and enjoys poking fun at overly enthusiastic motivational messages in the `demotivational.txt` file, it's important to recognize the seriousness of mental health. If you're feeling down or experiencing dark thoughts, please don't hesitate to reach out and talk to someone. Seeking support is a courageous step towards healing. You can also find resources and crisis lines specific to your country in this [list](https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines). 
Take care of yourself, and remember that you are not alone.