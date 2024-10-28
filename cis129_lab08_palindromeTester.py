# Lab 8 Palindrome Tester
# Name: Michaela Brady
# Date: 10/28/24
# Description: This program takes a string and determines if its a Palindrome, returning "true" if it is and "false" if it isn't.

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
  """
  Checks if a string is a palindrome, ignoring case, spaces, and punctuation.

  Args:
    text: The string to check.

  Returns:
    True if the string is a palindrome, False otherwise.
  """
  text = text.lower().replace(" ", "").replace(",", "").replace(".", "")
  s = Stack()
  for char in text:
    s.push(char)

  reversed_text = ''
  while not s.isEmpty():
    reversed_text += s.pop()

  return text == reversed_text
