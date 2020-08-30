'''
1. Two Sum
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        a = 0
        for i in nums:
            a += 1
            for j in nums[a:]:
                if i+j == target:
                    result.append(nums.index(i))
                    result.append(nums.index(j,a))
        return result;

listA = [3,2,4]
target = 6
print("\n Answer:", Solution.twoSum(None, listA, target))