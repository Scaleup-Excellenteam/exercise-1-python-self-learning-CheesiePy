from typing import Iterable, Any, List

def interleave(*args: Iterable[Any]) -> List[Any]:
    """Interleave multiple iterables."""
    res = []
    max_len = max(len(arg) for arg in args)

    for i in range(max_len):
        for j in range(len(args)):
            res.append(args[j][i])
    
    return res



def main():
    print(interleave('abc', [1, 2, 3], ('!', '@', '#'))) # ['a', 1, '!', 'b', 2, '@', 'c', 3, '#'])

if __name__=="__main__":
    main()