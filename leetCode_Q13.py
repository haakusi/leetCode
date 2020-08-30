'''
13. Roman to Integer
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Example 1:
Input: "IX"
Output: 9

Example 2:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3

Example 3:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res, p = 0, 'I'
        for c in s[::-1]:
            res, p = res - dic[c] if dic[c] < dic[p] else res + dic[c], c
        return res

strA = "MIVI"
print("\n Answer:", Solution.romanToInt(None, strA))