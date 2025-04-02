import string
text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""

def count_words(text):
    """
    Count the number of letters in each word in the given text."""
    words = (word.strip(string.punctuation) for word in text.split())
    return {word: len(word) for word in words if word.isalpha()}

def main():
    print(count_words(text))

if __name__=="__main__":
    main()
