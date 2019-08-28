class Solution:
    def is_valid(self, ip : List[str]):
        for token in ip:
            if int(token) > 255 or int(token) < 0:
                return None
            elif token[0] == '0' and len(token) != 1:
                return None
        return ip
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        num = len(s)
        for i in range(1, min(4,num-2)):
            for j in range(i+1, min(i+4,num-1)):
                for k in range(j+1,min(j+4,num)):
                    if num - k <= 3:
                        valid = self.is_valid([s[:i], s[i:j], s[j:k],s[k:]]) 
                        if valid != None:
                            result.append(".".join(valid))
        return result
                            
                    

