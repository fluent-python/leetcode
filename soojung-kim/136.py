from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        result = [num for num, cnt in counter.items() if cnt == 1]
        return result[0]


if __name__ == '__main__':
    inputs = [4,1,2,1,2]
    result = Solution().singleNumber(inputs)
    print(result)
