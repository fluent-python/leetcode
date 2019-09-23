class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha_dict = {}
        
        for ss in s:
            if ss in alpha_dict:
                alpha_dict[ss] += 1
            else:
                alpha_dict[ss] = 1
        
        for tt in t:
            if tt in alpha_dict:
                alpha_dict[tt] -= 1
                if alpha_dict[tt] < 0 :
                    return False
            else:
                return False
        
        for k, v in alpha_dict.items():
            if v != 0 :
                return False
        return True 
    
