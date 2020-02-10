from collections import Counter
from typing import List
import operator

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        majority_elm = max(counter.items(), key=operator.itemgetter(1))[0]
        return majority_elm


if __name__ == '__main__':
    nums = [3,2,3]
    result = Solution().majorityElement(nums)
    assert result == 3, 'Wrong answer'