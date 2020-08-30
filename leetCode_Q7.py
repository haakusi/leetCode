'''
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
'''
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if x >= 0:
            result = int(str(x)[::-1])
        else:
            result = int('-'+str(x)[:0:-1])
        return 0 if result > pow(2,31)-1 or result < -pow(2,31) else result;

intA = 1534236469
#intB = -321
print("\n Answer:", Solution.reverse(None, intA))