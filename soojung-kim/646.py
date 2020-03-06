from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-(k%len(nums))):
            nums.append(nums.pop(0))

if __name__ == '__main__':
    Solution().rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)