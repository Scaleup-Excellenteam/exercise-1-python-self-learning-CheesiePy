def cup_of_join(*args, sep='-'):
    """Join multiple iterables with a separator."""
    res = []
    for i in range(len(args)):
        res.extend(args[i])
        res.append(sep)
    return res


# Test cases
def test():
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))  # [1, 2, '@', 8, '@', 9, 5, 6]
    print(cup_of_join([1, 2], [8], [9, 5, 6]))  # [1, 2, '-', 8, '-', 9, 5, 6]
    print(cup_of_join([1]))  # [1]
    print(cup_of_join())  # None or error (as per your choice)

if __name__ == "__main__":
    test()