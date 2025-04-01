"""
group_by
כתבו פונקציה בשם group_by שמקבלת פונקציה כפרמטר ראשון, ו־iterable כפרמטר שני.
הפונקציה תחזיר מילון, שבו:
המפתחות הם הערכים שחזרו מהפונקציה שהועברה כפרמטר הראשון.
הערך התואם למפתח מסוים הוא רשימה של כל האיברים שעבורם חזר הערך המופיע במפתח.
לדוגמה, עבור הקריאה group_by(len, ["hi", "bye", "yo", "try"]) יוחזר הערך: {2: ["hi", "yo"], 3: ["bye", "try"]}
"""

from typing import Iterable, Dict, Any, List, Callable
def group_by(funcion : Callable, collaction : Iterable[Any]) -> Dict[Any, List[Any]]:
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
