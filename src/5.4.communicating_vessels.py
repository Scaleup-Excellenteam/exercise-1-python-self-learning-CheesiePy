from itertools import zip_longest
from typing import Iterable, Any, List

def interleave(*args: Iterable[Any]) -> List[Any]:
    """Interleave multiple iterables."""
    res = []
    max_len = max(len(arg) for arg in args)
    return [item for sublist in zip_longest(*args) for item in sublist]


def generator_interleave(*args: Iterable[Any]) -> Iterable[Any]:
    """Generate interleaved elements from multiple iterables using a generator."""
    max_len = max(len(arg) for arg in args)

    for i in range(max_len):
        for j in range(len(args)):
            if i < len(args[j]):
                yield args[j][i]
    


def main():
    print(interleave('abc', [1, 2, 3], ('!', '@', '#'))) # ['a', 1, '!', 'b', 2, '@', 'c', 3, '#'])

if __name__=="__main__":
    main()