class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # no extra space with O(N)
        result = 0
        for n in nums:
            result = result^n
        
        return result
