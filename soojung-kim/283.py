from typing import List
from collections import Counter

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        while 0 in nums:
            nums.remove(0)
        for i in range(counter[0]):
            nums.insert(len(nums), 0)
        print(nums)


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums=nums)


