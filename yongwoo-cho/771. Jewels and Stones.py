class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0 
        for i in range(len(J)):
            count+=S.count(J[i])
        return count
