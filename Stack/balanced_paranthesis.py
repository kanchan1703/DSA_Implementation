# Balanced Paranthesis
# Given string str containing just the characters '(', ')', '{', '}', '[' and ']'. 
# Check if the input string is valid and return true if the string is balanced otherwise return false.

def isBalanced(s):
    stack = []     # Initialise an empty stack to keep track of the opening brackets
    brackets = {')': '(', ']': '[', '}': '{'}  #Dictionary to map claosing brackets with opening brackets

    # traversing through the string
    for char in s:
        
