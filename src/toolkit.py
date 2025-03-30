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


def main():
    """
    Main function to generate empty solution files.
    """
    dir = os.path.dirname(__file__)
    dir = dir.replace('src', 'tests')
    files = get_files_name(dir)
    gen_solution_files(dir, files)
if __name__ == "__main__":
    main()
    