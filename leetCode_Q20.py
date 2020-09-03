'''
20. Valid Parentheses
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        left, right, stack = "([{", ")]}", []     # 변수 선언
        for item in s:              # str만큼 for문 동작
            if item in left:        # item이 (,[,{ 중에 있으면
                stack.append(item)    # lst에 추가한다.
                print("left",not stack, item)
            else:                   # item이 ),],} 중에 있으면
                print("right", right.find(item), item)
                if not stack or left.find(stack.pop()) != right.find(item):
                    return False
        return not stack      # True, 스택이 비어있다

'''
if stack is empty then if stack returns False
if stack is not empty then if stack returns True
isValid must return True when stack is empty so return not stack
'''
strA = "{[]}"
print("\n Answer:", Solution.isValid(None, strA))