import copy 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [[nums[0]]]
        elif len(nums) == 2:
            return [[nums[0],nums[1]],[nums[1],nums[0]]]
 
        
        for i in nums:
            tmp = [i]
            next_input = copy.deepcopy(nums)
            next_input.remove(i)
            # print(next_input)
            
            for outputs in self.permute(next_input):
                result.append(tmp+outputs)
        
        return result
        
