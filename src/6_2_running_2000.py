
import time 
def timer(func, *args, **kwargs):
    """
    A decorator to measure the execution time of a function."""
    start = time.time()

    func(*args, **kwargs)

    end = time.time()

    function_name = func.__name__

    elapsed_time = end - start
    print(f"Function '{function_name}' took {elapsed_time:.6f} seconds to execute with arguments {args or kwargs}.")


def main():
    timer(print, "Hello") #, תחזיר הפונקציה את משך זמן הביצוע של print("Hello").
    timer(zip, [1, 2, 3], [4, 5, 6])# , תחזיר הפונקציה את משך זמן הביצוע של zip([1, 2, 3], [4, 5, 6]).
    timer("Hi {name}".format, name="Bug") # , תחזיר הפונקציה את משך זמן הביצוע של "Hi {name}".format(name="Bug")

if __name__=="__main__":
    main()