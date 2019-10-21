from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s_ns = sorted(nums)
        return s_ns[len(nums) // 2]

s = Solution()
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([2, 2, 2, 1, 1, 1, 2]))
