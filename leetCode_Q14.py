'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
'''

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        if strs[0] == '': return ''

        res, c = strs[0][0], 1

        while c <= len(strs[0]):    # 첫글자부터 끝문자까지
            for w in strs:          # 주어진 Input 배열들을 w로 돌린다
                if res != w[:len(res)]:     # 첫글자 부터 추가된 것들이 현재 비교되는 w[:len(res)]와 다를 경우 return
                    return res[:-1]
            if c >= len(strs[0]):       # 마지막까지 돌았는데 같을경우 브레이크
                break
            res += strs[0][c]       # 첫번째 Input의 문자(res)에 이후 문자(c)를 하나씩 계속 붙여나간다.
            c += 1         # 다음 문자열 위치값 1씩 증
        return res

#listA = ["Class", "Cliche", "Cllli"]
listA = ["Class", "Clb"]
print("\n Answer:", Solution.longestCommonPrefix(None,listA))