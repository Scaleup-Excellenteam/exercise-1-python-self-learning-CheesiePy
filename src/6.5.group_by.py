from typing import Iterable, Dict, Any, List, Callable
def group_by(funcion : Callable, collaction : Iterable[Any]) -> Dict[Any, List[Any]]:
    """Groups elements of a collection by a function.
    Args:
        funcion (Callable): A function to group the elements.
        collaction (Iterable[Any]): The collection to group.
    Returns:
        Dict[Any, List[Any]]: A dictionary where the keys are the results of the function and the values are lists of elements that produced that key.
    """
    if not callable(funcion):
        raise ValueError("The first argument must be a callable function.")
    if not isinstance(collaction, Iterable):
        raise ValueError("The second argument must be an iterable collection.")
    if not isinstance(collaction, (list, tuple)):
        raise ValueError("The second argument must be a list or tuple.")
    
    res = {}
    for item in collaction:
        key = funcion(item)
        if key not in res:
            res[key] = []
        res[key].append(item)

    return res


def main():
    print(group_by(len, ["hi", "bye", "yo", "try"])) # {2: ["hi", "yo"], 3: ["bye", "try"]}


if __name__=="__main__":
    main()
