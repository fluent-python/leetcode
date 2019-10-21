import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)/2
        c_dict = collections.Counter(nums)
        for k, v in c_dict.items():
            if v > N:
                return k
        
