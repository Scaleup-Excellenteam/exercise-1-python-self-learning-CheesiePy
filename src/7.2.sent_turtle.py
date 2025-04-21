class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
    
        # validate usernames
        if not isinstance(usernames, list):
            raise TypeError("Usernames must be a list.")
        if not all(isinstance(user, str) for user in usernames):
            raise TypeError("All usernames must be strings.")
        if len(usernames) < 2:
            raise ValueError("At least two usernames are required.")
            

        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

        
    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        if recipient not in self.boxes:
            raise KeyError(f"Recipient {recipient} does not exist.")
        if sender not in self.boxes:
            raise KeyError(f"Sender {sender} does not exist.")
        if not isinstance(message_body, str):
            raise TypeError("Message body must be a string.")
        if not isinstance(urgent, bool):
            raise TypeError("Urgency must be a boolean.")
        


        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, num_messages=None):
        """Read the inbox of a user.

        :param str username: The user's username.
        :param int num_messages: The number of messages to read.
        :return: List of messages read.
        :rtype: list
        """
        # Validate username
        if username not in self.boxes:
            raise KeyError(f"User {username} does not exist.")
        if not isinstance(num_messages, (int, type(None))):
            raise TypeError("num_messages must be an integer or None.")
        if num_messages is not None and num_messages < 0:
            raise ValueError("num_messages must be a non-negative integer.")
        if num_messages == 0:
            return []

        user_box = self.boxes[username]
        if num_messages is None:
            num_messages = len(user_box)
        messages = user_box[:num_messages]
        del user_box[:num_messages]
        return messages
    
    def search_inbox(self, username, search_string):
        """Search the inbox of a user for a specific string.

        :param str username: The user's username.
        :param str search_string: The string to search for.
        :return: List of messages containing the search string.
        :rtype: list
        """
        # Validate username
        if username not in self.boxes:
            raise KeyError(f"User {username} does not exist.")
        if not isinstance(search_string, str):
            raise TypeError("search_string must be a string.")
        if not search_string:
            raise ValueError("search_string cannot be empty.")
    

        user_box = self.boxes[username]
        messages = [message for message in user_box if search_string in message['body']]
        return messages


def main():
    po = PostOffice(['Alice', 'Bob', 'Charlie'])
    po.send_message('Alice', 'Bob', 'Hello Bob!')
    po.send_message('Bob', 'Alice', 'Hi Alice!')
    po.send_message('Charlie', 'Alice', 'Hey Alice!', urgent=True)
    print(po.read_inbox('Alice'))
    print(po.search_inbox('Alice', 'Hello'))

if __name__ == "__main__":
    main()
