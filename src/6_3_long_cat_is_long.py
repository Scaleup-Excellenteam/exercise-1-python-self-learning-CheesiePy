"""
חתול ארוך הוא ארוך
כתבו פונקציה בשם count_words שמקבלת כפרמטר טקסט, ומחזירה מילון של אורכי המילים שבו.
השתמשו ב־comprehension לבחירתכם (או ב־generator expression) כדי לנקות את הטקסט מסימנים שאינם אותיות.
לאחר מכן, השתמשו ב־dictionary comprehension כדי לגלות את אורכה של כל מילה במשפט.
לדוגמה, עבור הטקסט הבא, בדקו שחוזר לכם המילון המופיע מייד אחריו.
import string


expected_result = {'you': 3, 'see': 3, 'wire': 4, 'telegraph': 9, 'is': 2, 'a': 1, 'kind': 4, 'of': 2, 'very': 4, 'long': 4, 'cat': 3, 'pull': 4, 'his': 3, 'tail': 4, 'in': 2, 'new': 3, 'york': 4, 'and': 3, 'head': 4, 'meowing': 7, 'los': 3, 'angeles': 7, 'do': 2, 'understand': 10, 'this': 4, 'radio': 5, 'operates': 8, 'exactly': 7, 'the': 3, 'same': 4, 'way': 3, 'send': 4, 'signals': 7, 'here': 4, 'they': 4, 'receive': 7, 'them': 4, 'there': 5, 'only': 4, 'difference': 10, 'that': 4, 'no': 2}
"""

text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""
import string
def count_words(text):
    words = (word.strip(string.punctuation) for word in text.split())
    return {word: len(word) for word in words if word.isalpha()}

def main():
    print(count_words(text))

if __name__=="__main__":
    main()