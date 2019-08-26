class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        original_length = len(arr)
        for idx in range(original_length-1,-1,-1):
            if arr[idx] == 0 :
                arr.insert(idx+1,0)
                arr.pop()
