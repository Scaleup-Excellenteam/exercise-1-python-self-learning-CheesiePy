import os

def search_in_folder(dir, phrase):
    """
    return a list on names of files in dir that thier name contain phrase. 
    """
    # validate inputs
    if not os.path.isdir(dir):
        raise ValueError(f"{dir} is not a valid directory")
    

    files = []
    for root, dirs, filenames in os.walk(dir):
        for filename in filenames:
            if phrase in filename:
                files.append(filename)
    return files

            

def thats_the_way(dir):
    """
    This function prompts the user for a directory and a phrase, then searches for files in the directory that contain the phrase.
    """
    # dir = input("Enter the directory to search: ")
    # phrase = input("Enter the phrase to search for: ")
    phrase = "deep"
    try:
        files = search_in_folder(dir, phrase)
    except ValueError as e:
        exit(f"Error: {e}")
    
    if files:
        print(f"Files containing '{phrase}':")
        for file in files:
            print(file)
    else:
        print(f"No files found containing '{phrase}'.")

if __name__ == "__main__":
    thats_the_way()