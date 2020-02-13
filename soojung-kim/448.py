from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int])-> List[int]:
        origin_num_list = [i for i in range(1, len(nums)+1)]
        return list(set(origin_num_list).difference(set(nums)))


if __name__ == '__main__':
    result = Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])
    assert result == [5, 6], "Wrong answer"