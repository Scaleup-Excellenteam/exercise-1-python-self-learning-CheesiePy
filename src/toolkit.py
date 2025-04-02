# this is a toolkit module to generate empty solution files and to help me with the assignments
import os

def get_files_name(dir):
    """
    Get all the files in the given directory.
    remove the test_ prefix and add the .py suffix.
    return the list of file names.
    """
    files = []
    for file in os.listdir(dir):
        if file.startswith("test_") and file.endswith(".py"):
            files.append(file[5:-3] + ".py")
    return files

def gen_solution_files(files):
    """
    Generate empty solution files for the given files.
    :param dir: The directory to create the files in.
    :param files: The list of file names to create.
    """
    dir = os.path.dirname(__file__)
    for file in files:
        with open(os.path.join(dir, file), 'w') as f:
            pass
    print(f"Created {len(files)} empty solution files in {dir}")

def change_files_names(dir, files, sep):
    """
    if this is the file name 5_1_thats_the_way.py change it to 5.1.thats_the_way.py 
    """
    for file in files:
        if file.endswith(".py"):
            new_file = file.replace("_", sep)
            os.rename(os.path.join(dir, file), os.path.join(dir, new_file))
            print(f"Renamed {file} to {new_file}")
    

def main():
    """
    Main function to generate empty solution files.
    """


    # Get the directory of the current file
    # dir = os.path.dirname(__file__)
    # dir = dir.replace('src', 'tests')
    # files = get_files_name(dir)
    # gen_solution_files(dir, files)


    # Change the file names to the new format
    dir = os.path.dirname(__file__)
    files = os.listdir(dir)
    sep = "."
    change_files_names(dir, files, sep)
    
if __name__ == "__main__":
    main()
    