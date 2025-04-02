from typing import Iterable, Dict, Any, List, Callable
def group_by(funcion : Callable, collaction : Iterable[Any]) -> Dict[Any, List[Any]]:
    """Groups elements of a collection by a function."""
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
