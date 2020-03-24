from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        counter_1 = Counter(nums1)
        counter_2 = Counter(nums2)
        keys = list(set(counter_1.keys()).intersection(counter_2.keys()))
        result = []

        for i in keys:
            iter = min(counter_1[i], counter_2[i])
            for _ in range(iter):
                result.append(i)
        result.sort()
        return result


if __name__ == '__main__':
    nums1 = [1, 1]
    nums2 = [1, 2]
    result = Solution().intersect(nums1, nums2)
    print(result)