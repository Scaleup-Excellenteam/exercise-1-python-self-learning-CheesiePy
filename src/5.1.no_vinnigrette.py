import random
from datetime import datetime, timedelta
import sys

def random_date_from_range(start_date="2023-07-10", end_date="2023-07-10"):
    """
    Generates a random date between start_date and end_date.
    """
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        delta = end - start
        random_days = random.randint(0, delta.days)
        return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")
    except ValueError:
        print("Try YYYY-MM-DD as format for you")

def no_vinnigrete():
    """This function generates a random date between two given dates and checks if the date is a Monday."""
    if len(sys.argv) == 3: # if you want to work it as cli tool
        start_date = sys.argv[1]
        end_date = sys.argv[2]
        random_date = random_date_from_range(start_date, end_date)
    # if random date is Monday
    while random_date == None:
        start_date = input("Please Enter Start Date in Valid format Date YYYY-MM-DD: ")
        end_date = input("Please Enter End Date in Valid format Date YYYY-MM-DD: ")
        random_date = random_date_from_range(start_date, end_date)
    datetime_object = datetime.strptime(random_date, "%Y-%m-%d")
    

    if datetime_object.weekday == 0: # moday is 0
        print("No Vinnigerette")
    else:
        print(f'{random_date}')

if __name__ == "__main__":
    no_vinnigrete()

