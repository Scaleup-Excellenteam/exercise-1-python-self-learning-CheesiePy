from functools import wraps

def type_check(currect_type):
    """this will be a decorator that does a type check for a function and if its not the currect one it raise an eception"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, currect_type):
                    raise Exception(f"wront typing! you enterd {type(arg)}, while you should have entered {currect_type}")
            return func(*args, **kwargs)
        return wrapper
    return decorator 
        

@type_check(int)
def times2(num):
    return num*2

def test():
    try:
        print(times2(3))
        print(times2("3"))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    test()