# Problem: Valid Parentheses
# Link to LeetCode problem: https://leetcode.com/problems/valid-parentheses/
#
# Description:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
#
# An input string is valid if:
#   1. Open brackets are closed by the same type of brackets.
#   2. Open brackets are closed in the correct order.
#   3. Every closing bracket has a corresponding open bracket of the same type.

# ------------------------------------------------------------
# 🧠 Solution Approaches:
# 1) Brute Force:
#    - Repeatedly remove valid pairs ("()", "{}", "[]") from the string.
#    - If the final string is empty, it's valid.
#    - Time Complexity: O(n^2)
#    - Space Complexity: O(n)
#
# 2) Efficient (Two Variants):
#    - Use a stack to track opening brackets.
#    - Use a dictionary for bracket matching.
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)
# ------------------------------------------------------------

# 🧪 Brute Force Implementation
def isValid_brute_force(s: str) -> bool:
    prev_length = -1
    while prev_length != len(s):
        prev_length = len(s)
        s = s.replace("()", "").replace("{}", "").replace("[]", "")
    return s == ""

# ⚡ Efficient Implementation — Matching: opening → closing
def isValid_efficient_opening_map(s: str) -> bool:
    stack = []
    matching = {'(': ')', '{': '}', '[': ']'}
    
    for char in s:
        if char in matching:  # opening bracket
            stack.append(char)
        else:  # closing bracket
            if not stack:
                return False
            top = stack.pop()
            if matching[top] != char:
                return False

    return not stack

# ⚡ Efficient Implementation — Matching: closing → opening
def isValid_efficient_closing_map(s: str) -> bool:
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching.values():  # opening bracket
            stack.append(char)
        elif char in matching:  # closing bracket
            if not stack or stack.pop() != matching[char]:
                return False
        else:
            return False  # unexpected character

    return not stack
