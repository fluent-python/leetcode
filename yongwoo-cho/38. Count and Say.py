class Solution:
    def calcNext(self,n):
        result = []
        before = n[0]
        count = 1
        for i in n[1:]:
            if before == i:
                count += 1
            else:
                result.append(str(count))
                result.append(str(before))
                count = 1
            before = i
        result.append(str(count))
        result.append(str(before))
        
        return ''.join(result)
    def countAndSay(self, n: int) -> str:
        num = "1"
        for i in range(n-1):
            num = self.calcNext(num)       
        return num
                
            
