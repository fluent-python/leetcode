from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = 0
        cur_max = 0

        for idx, num in enumerate(nums):
            cur_max = cur_max + num
            if cur_max < 0:
                cur_max = 0
            if result < cur_max:
                result = cur_max
        return result


if __name__ == '__main__':
    Input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output = 6
    # Explanation: [4, -1, 2, 1]
    # sum = 6.
    result = Solution().maxSubArray(Input)
    assert result == Output