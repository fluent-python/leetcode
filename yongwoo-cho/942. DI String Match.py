class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        result = []
        max_num = len(S)
        min_num = 0
            
        for i in S:
            if i == "I":
                result.append(min_num)
                min_num += 1
            else :
                result.append(max_num)
                max_num -=1
        result.append(max_num)
        return result
            
            
            
