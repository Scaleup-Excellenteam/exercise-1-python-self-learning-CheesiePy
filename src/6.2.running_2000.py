
import time 
def running_2000(func, *args, **kwargs):
    """
    A decorator to measure the execution time of a function."""

    if not callable(func):
        raise ValueError("The first argument must be a callable function.")
    if not isinstance(args, tuple):
        raise ValueError("The second argument must be a tuple of positional arguments.")
    if not isinstance(kwargs, dict):
        raise ValueError("The third argument must be a dictionary of keyword arguments.")
    

    start = time.time()

    func(*args, **kwargs)

    end = time.time()

    function_name = func.__name__

    elapsed_time = end - start
    print(f"Function '{function_name}' took {elapsed_time:.6f} seconds to execute with arguments {args or kwargs}.")


def main():
    running_2000(print, "Hello") #, תחזיר הפונקציה את משך זמן הביצוע של print("Hello").
    running_2000(zip, [1, 2, 3], [4, 5, 6])# , תחזיר הפונקציה את משך זמן הביצוע של zip([1, 2, 3], [4, 5, 6]).
    running_2000("Hi {name}".format, name="Bug") # , תחזיר הפונקציה את משך זמן הביצוע של "Hi {name}".format(name="Bug")

if __name__=="__main__":
    main()
