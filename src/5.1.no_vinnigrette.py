import random
from datetime import datetime, timedelta
import sys

def random_date_from_range(start_date="2023-07-10", end_date="2023-07-10"):
    """
    Generates a random date between start_date and end_date.
    Args:
    - start_date (str): The start date in YYYY-MM-DD format.
    - end_date (str): The end date in YYYY-MM-DD format.
    Returns:
    - str: A random date in YYYY-MM-DD format.
    Raises:
    - ValueError: If the input date format is incorrect.
    """
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        delta = end - start
        random_days = random.randint(0, delta.days)
        return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")
    except ValueError:
        raise("Try YYYY-MM-DD as format for you")

def no_vinnigrete():
    """
    This function generates a random date between two given dates and checks if the date is a Monday.
    output:
    - If the date is a Monday, it prints "No Vinnigerette".
    - If the date is not a Monday, it prints the date.
    Args:
    - None (function does not take any arguments but reads from standard input).
    Returns:
    - str: A message indicating whether the date is a Monday or not.
        """
    # if len(sys.argv) == 3: # if you want to work it as cli tool
    #     start_date = sys.argv[1]
    #     end_date = sys.argv[2]
    #     random_date = random_date_from_range(start_date, end_date)
    
    
    # read from standard input
    random_date = None


    # if random date is Monday
    while random_date == None:
        start_date = input("Please Enter Start Date in Valid format Date YYYY-MM-DD: ")
        end_date = input("Please Enter End Date in Valid format Date YYYY-MM-DD: ")
        random_date = random_date_from_range(start_date, end_date)
    datetime_object = datetime.strptime(random_date, "%Y-%m-%d")
    

    if datetime_object.weekday == 0: # moday is 0
        return "No Vinnigerette"
    else:
        return random_date

if __name__ == "__main__":
    no_vinnigrete()

