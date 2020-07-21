from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        freq = Counter(nums)
        res = [k for k, v in sorted(freq.items(), key=(lambda x: x[1]), reverse=True)]
        return res[:k]





if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    k = 2

    res = Solution().topKFrequent(nums, k)
    print(res)