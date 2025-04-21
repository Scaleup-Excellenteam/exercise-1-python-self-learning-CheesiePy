

import cv2
from typing import List

def remember_remember(path: str) -> str:
    """Reads a black and white image and returns the characters represented by non-white pixels."""
    with open(path, 'rb') as f:
        if not f.read():
            raise ValueError("File is empty or not a valid image.")
    
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Could not read the image file.")
    height, width = img.shape
    message = ""
    for col in range(width):
        for row in range(height):
            if img[row, col] != 255:  # non-white pixel
                message += chr(row)
    return message

def main():
    path = 'resources/code.png'
    message = remember_remember(path)
    print(message)

if __name__ == "__main__":
    main()
