def parsle_tongue():
    """
    This function reads a binary file and extracts secret messages from it.
    The messages are strings of lowercase English letters that end with an exclamation mark.
    """
    secret_messages = []
    chunck_read_flag = True
    with open("resources/logo.jpg", "rb") as file:
        while flag:
            # chuck should contain at least 5 characters witch is 5*4=20 bytes
            chunk = file.read(20)
            if not chunk:
                flag = False
                # End of file reached
                break
            # Decode the chunk to a string
            decoded_chunk = chunk.decode(errors='ignore')
            # Find all secret messages in the decoded chunk
            for word in decoded_chunk.split():
                if len(word) >= 5 and word.islower() and word.endswith('!'):
                    secret_messages.append(word)
    return secret_messages

def main():
    """
    Main function to run the parsle_tongue function and print the secret messages.
    """
    messages = parsle_tongue()
    for message in messages:
        print(message)

if __name__ == "__main__":
    main()