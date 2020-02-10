class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        success = 0
        def isNondecreasing(num_list):
            for i in range(len(num_list)-1):
                if num_list[i] > num_list[i+1]:
                    return False
            return True
                    
                
            
        for i in range(len(nums) -1):
            if nums[i] > nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                print(success)
                success = isNondecreasing(nums)
                nums[i] = temp
                print(success)

                if success == 1:
                    return True
                
                nums[i+1] = nums[i]
                success = isNondecreasing(nums)
                print(success)

                if success == 1:
                    return True
                
                else :
                    return False

        return True
                
            
