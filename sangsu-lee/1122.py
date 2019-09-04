
from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        new_arr = []

        for d_item in arr2:
            while d_item in arr1:
                arr1.remove(d_item)
                new_arr.append(d_item)
        return new_arr + sorted(arr1)
