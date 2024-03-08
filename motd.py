import random
import os
from typing import List
import attr


@attr.s
class MOTD:
    """
    Class to manage Messages of the Day (MOTD).

    Attributes:
        file_path (str): The path to the file containing MOTD messages.
        previous_message (str): The previous MOTD message.
    """

    file_path: str = attr.ib(default="data/")
    previous_message: str = attr.ib(default="")

    def get_random_message_from_file(self) -> str:
        """
        Retrieve a random message from the specified file.

        Returns:
            str: A random MOTD message from the file.
        """
        with open(self.file_path, "r") as file:
            messages = file.readlines()
            random_message = random.choice(messages).strip()
        return random_message

    def get_random_message_from_catalogue(self) -> str:
        """
        Retrieve a random message from a random .txt file in the specified folder.

        Returns:
            str: A random MOTD message from a .txt file.
        """
        file_list = [f for f in os.listdir(self.file_path) if f.endswith(".txt")]

        if not file_list:
            return "No .txt files found in the data folder."

        random_file = random.choice(file_list)
        full_path = os.path.join(self.file_path, random_file)

        with open(full_path, "r") as file:
            lines = file.readlines()
            random_message = random.choice(lines).strip()

        # Ensure the same message is not repeated consecutively
        while random_message == self.previous_message:
            random_message = random.choice(lines).strip()

        self.previous_message = random_message
        return random_message

    def set_message(self, message: str) -> None:
        """
        Set a specific message as the current MOTD.

        Args:
            message (str): The MOTD message to set.
        """
        self.previous_message = message

    def get_message(self) -> str:
        """
        Retrieve the current MOTD.

        Returns:
            str: The current MOTD message.
        """
        return self.previous_message
