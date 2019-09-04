class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        non_relative = []
        relative = {}
        result =[]
        for value in arr2:
            relative[value] = arr1.count(value)
        
        for value in arr1:
            if value not in relative:
                non_relative.append(value)
        
        for value in arr2:
            result +=[value] * relative[value]
        
        non_relative.sort()
        return result + non_relative
            
            
            
            
