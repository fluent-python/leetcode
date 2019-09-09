class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_dict = {}
        believe_dict = {}
        if N == 1:
            return 1
        for i in trust:
            if i[1] in trust_dict:
                trust_dict[i[1]] += 1
            else:
                trust_dict[i[1]] = 1
            
            if i[0] in believe_dict:
                believe_dict[i[0]] +=1
            else :
                believe_dict[i[0]] = 1
            
        for k, v in trust_dict.items():
            if v == N-1 and believe_dict.get(k) == None:
                return k
        
        return -1
                
        
