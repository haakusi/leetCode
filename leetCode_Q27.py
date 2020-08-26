'''
27. Remove Element
Given an array nums and a value val, remove all instances of
that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

The order of elements can be changed.
It doesn't matter what you leave beyond the new length.

Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
Note that the order of those five elements can be arbitrary.
It doesn't matter what values are set beyond the returned length.
'''

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        i = 0
        while i < len(nums):        # 주어진 배열 nums 처음부터 길이만큼 돌린다.
            if nums[i] == val:      # 그 과정에서 주어진 val과 같은 값이 있으면
                nums.pop(i)         # 배열안에서 해당위치 배열 값을 pop(i) 해준다.
            else:
                i+=1
        return len(nums)            # 제거되고 남은 결과값을 return 한다.

#nums = [0, 1, 2, 2, 0, 3, 4, 0, 2]
nums = [3,2,2,3]
val = 3
print("\n Answer:", Solution.removeElement(None, nums, val))
