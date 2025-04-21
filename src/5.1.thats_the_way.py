import os

def thats_the_way(dir):
    """
    This function prompts the user for a directory and a phrase, then searches for files in the directory that contain the phrase.
    Args:
    - dir (str): The directory to search in.
    Returns:
    - list: A list of files in the directory that contain the phrase.
    Raises:
    - ValueError: If the directory is not valid.
    """
    phrase = "deep"
    # validate dir 
    if not os.path.isdir(dir):
        raise ValueError(f"{dir} is not a valid directory")
    
    #return list comprehension added to get the files
    return [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f)) and f.startswith(phrase)]

if __name__ == "__main__":
    files = thats_the_way()
    print(f'list of files that start with the phrase "deep": {files}')