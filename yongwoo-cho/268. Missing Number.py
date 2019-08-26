class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_length = len(nums)
        
        expected_sum = ((num_length+1)* num_length )/2
        return int(expected_sum  - sum(nums))
