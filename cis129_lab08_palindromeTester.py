# Palindrome Tester
# Checks if a given string is a palindrome, ignoring case, spaces, and punctuation.
# Michaela Brady
# 10/28/24


import re


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def is_palindrome(text):
    # Ignore case, spaces, and punctuation

    text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    s = Stack()
    for char in text:
        s.push(char)

    reversed_text = ''
    while not s.isEmpty():
        reversed_text += s.pop()

    return text == reversed_text
# Test cases
print(is_palindrome("mom"))  # True
print(is_palindrome("dude"))    # False
print(is_palindrome("level"))  # True
