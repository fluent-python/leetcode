class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        if len(nums) == 0:
            return result
        if target < nums[0]:
            return result
        if target > nums[-1]:
            return result
        
        start = 0
        end = len(nums)
        search_idx = int((start+end) //2)
        # binary search
        while nums[search_idx] != target:
            if nums[search_idx] > target:
                end  = search_idx
            else:
                start = search_idx +1
                
            search_idx = int((start + end) //2)
            
            if start >= end:
                return result
        
        left = search_idx
        right = search_idx
        tmp = 1
        
        
        while True:
            print(search_idx,left,right)
            if nums[left] == nums[search_idx]:
                result[0] = left
            if nums[right] == nums[search_idx]:
                result[1] = right
            if left == 0 and right == len(nums)-1:
                return result
            left -= tmp
            right += tmp
            if left < 0:
                left  = 0
            if right >= len(nums):
                right = len(nums)-1
          
            if nums[left] != nums[search_idx] and nums[right] != nums[search_idx]:
                break;
        
        return result
        
