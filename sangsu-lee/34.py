from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        start_ix = nums.index(target)
        nums = list(reversed(nums))
        end_ix = len(nums) - nums.index(target) - 1
        return [start_ix, end_ix]
s = Solution()

print(s.searchRange([5,7,7,8,8,10], 8))
print(s.searchRange([5,7,7,8,8,10], 6))
print(s.searchRange([5,7,7,8,8,9,10], 9))
