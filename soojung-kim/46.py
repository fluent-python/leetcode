from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        results = []
        for i in range(len(nums)):  # 0, 1, 2
            s = nums[i]
            remList = nums[:i] + nums[i + 1:]
            for p in self.permute(remList):
                results.append([s] + p)
        return results

