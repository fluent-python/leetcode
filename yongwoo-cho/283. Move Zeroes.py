class Solution:
        
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_idx = len(nums)
        non_zero_idx = -1
        
        i = 0 
        while i < len(nums):
            if nums[i] == 0:
                zero_idx = min(i, zero_idx)
            else :
                non_zero_idx = i
            
            if zero_idx  < non_zero_idx:
                i = zero_idx
                nums[zero_idx], nums[non_zero_idx] = nums[non_zero_idx], nums[zero_idx]
                zero_idx = len(nums)
                non_zero_idx = i
            i+=1
        
            
            
            
            
        
